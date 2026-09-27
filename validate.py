#!/usr/bin/env python3
"""Validate data without importing or executing submitted effect code."""
import json
import math
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parent

def effect(data):
    assert set(data) == {'version', 'id', 'name', 'authorID', 'author', 'summary', 'license', 'credit', 'layers'}
    assert data['version'] == 1
    for key in ['id', 'authorID']:
        assert re.fullmatch(r'[A-Za-z0-9._-]{1,100}', data[key]), key
    for key, limit in [('name',60),('author',60),('summary',240),('credit',240)]:
        assert isinstance(data[key], str) and len(data[key]) <= limit
        assert not any(unicodedata.category(c) in {'Cc', 'Cf'} for c in data[key])
    assert data['name'].strip() and data['author'].strip()
    assert data['license'] in {'CC0-1.0', 'CC-BY-4.0'}
    assert 1 <= len(data['layers']) <= 6
    count = 0
    for layer in data['layers']:
        assert set(layer) == {'kind','motion','color','count','radius','width','opacity','period'}
        assert layer['kind'] in {'ring','rays','glow'}
        assert layer['motion'] in {'expand','contract','orbit','pulse'}
        assert re.fullmatch(r'#[A-Fa-f0-9]{6}', layer['color'])
        assert type(layer['count']) is int and 1 <= layer['count'] <= 80
        count += layer['count']
        for key, low, high in [('radius',8,600),('width',.5,16),('opacity',.05,1),('period',.5,8)]:
            value = layer[key]
            assert type(value) in {float,int} and math.isfinite(value) and low <= value <= high
    assert count <= 240

catalog_path = ROOT / 'catalog.json'
assert catalog_path.stat().st_size <= 512 * 1024
catalog = json.loads(catalog_path.read_text())
assert set(catalog) == {'version','effects'} and catalog['version'] == 1
assert len(catalog['effects']) <= 100
ids = set()
for entry in catalog['effects']:
    effect(entry)
    assert entry['id'] not in ids
    ids.add(entry['id'])
    path = ROOT / 'effects' / (entry['id'] + '.cfeffect')
    assert path.is_file() and path.stat().st_size <= 64 * 1024
    assert json.loads(path.read_text()) == entry
assert {p.stem for p in (ROOT/'effects').glob('*.cfeffect')} == ids
print(f'PASS: {len(ids)} validated, bounded effect definitions')
