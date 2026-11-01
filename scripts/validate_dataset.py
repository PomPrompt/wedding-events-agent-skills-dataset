#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate dataset snapshot files WITHOUT network activity or Skill execution."""
from pathlib import Path
from urllib.parse import urlparse
import csv, json, collections, sys, re, datetime

if not __debug__:
    raise RuntimeError('Do not execute this validator with Python -O: assertions must stay enabled.')

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
SCHEMA = json.loads((ROOT/'schema/06_DATASET01_SCHEMA.json').read_text(encoding='utf-8'))
RECORDS = json.loads((DATA/'WEDDING_EVENTS_SKILLS_DATASET01.json').read_text(encoding='utf-8'))
with (DATA/'WEDDING_EVENTS_SKILLS_DATASET01.csv').open(newline='',encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    columns = reader.fieldnames
    csv_records = list(reader)
expected_columns = SCHEMA['items']['required']
assert columns == expected_columns, 'CSV field order differs from required schema order'
assert len(RECORDS) == len(csv_records), 'CSV/JSON row counts differ'
assert len(RECORDS) > 0, 'Dataset empty'
ids, urls = set(), set()
cat_ids = set(SCHEMA['items']['properties']['primary_category']['enum'])
status_ids = set(SCHEMA['items']['properties']['link_check_status']['enum'])
scopes = set(SCHEMA['items']['properties']['scope']['enum'])
for i,(data,csvrow) in enumerate(zip(RECORDS,csv_records),1):
    assert list(data) == expected_columns, f'JSON schema keys mismatch in record {i}'
    assert re.fullmatch(r'WES-[0-9]{4,}',data['id']), f'Invalid ID: {data["id"]}'
    assert data['id'] not in ids, f'Duplicate ID: {data["id"]}'
    ids.add(data['id'])
    assert data['skill_url'] not in urls, f'Duplicate skill URL: {data["skill_url"]}'
    urls.add(data['skill_url'])
    assert data['primary_category'] in cat_ids
    assert data['relevance_tier'] in ('A','B'), 'Core records must be A/B'
    assert data['link_check_status'] in status_ids
    assert data['scope'] in scopes
    assert isinstance(data['tags'],list) and len(set(data['tags']))==len(data['tags'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}',data['discovered_at'])
    datetime.date.fromisoformat(data['discovered_at'])
    for field in ('skill_url','discovery_page_url','evidence_url'):
        addr=urlparse(data[field]);assert addr.scheme in ('https','http') and addr.netloc, f'Bad URL: {field}'
    assert csvrow['tags'] == '|'.join(data['tags']),f'Tags mismatch: {data["id"]}'
    for field in expected_columns:
        if field!='tags': assert csvrow[field] == str(data[field]),f'Field mismatch {data["id"]}/{field}'
try:
    import jsonschema
except ImportError:
    print('JSON Schema validation: skipped (install jsonschema for full Draft 2020-12 validation)')
else:
    from jsonschema import Draft202012Validator,FormatChecker
    Draft202012Validator(SCHEMA,format_checker=FormatChecker()).validate(RECORDS)
    print('JSON Schema validation: PASSED (Draft 2020-12)')
counts=collections.Counter(r['source_website'] for r in RECORDS)
with (DATA/'SOURCES_USED.csv').open(newline='',encoding='utf-8-sig') as file: sources=list(csv.DictReader(file))
assert sum(int(r['unique_core_records']) for r in sources)==len(RECORDS)
for source in sources:
    assert int(source['unique_core_records'])==counts[source['source_domain']], f'Count mismatch: {source["source_domain"]}'
with (DATA/'LEADS_PENDING.csv').open(newline='',encoding='utf-8-sig') as file: leads=list(csv.DictReader(file))
with (DATA/'DUPLICATE_MAP.csv').open(newline='',encoding='utf-8-sig') as file: duplicates=list(csv.DictReader(file))
assert all(d['retained_skill_url'] in urls for d in duplicates)
assert all(d['duplicate_candidate_url'] not in urls for d in duplicates)
assert all(r['candidate_url'] not in urls for r in leads)
print(f'PASS — {len(RECORDS)} core records, {len(leads)} leads, {len(duplicates)} alternate URLs, {len(counts)} sources')
print('Tier:',dict(collections.Counter(r['relevance_tier'] for r in RECORDS)))
print('Link status:',dict(collections.Counter(r['link_check_status'] for r in RECORDS)))
print('No web fetch or Skill execution performed.')

# Site mirrors exist only for optional static-page deployment; keep every copy identical.
MIRRORS = {
    'WEDDING_EVENTS_SKILLS_DATASET01.csv': DATA/'WEDDING_EVENTS_SKILLS_DATASET01.csv',
    'WEDDING_EVENTS_SKILLS_DATASET01.json': DATA/'WEDDING_EVENTS_SKILLS_DATASET01.json',
    'SOURCES_USED.csv': DATA/'SOURCES_USED.csv',
    'LEADS_PENDING.csv': DATA/'LEADS_PENDING.csv',
    'DUPLICATE_MAP.csv': DATA/'DUPLICATE_MAP.csv',
    'COLLECTION_REPORT.md': ROOT/'docs/COLLECTION_REPORT.md',
    'DATA_DICTIONARY.md': ROOT/'docs/DATA_DICTIONARY.md',
}
for name, original in MIRRORS.items():
    copy = ROOT/'site/data'/name
    assert copy.is_file(), f'Missing site mirror {copy}'
    assert copy.read_bytes() == original.read_bytes(), f'Stale site mirror: {copy}'
print('Site asset mirrors: PASS (all 7 byte-identical)')
