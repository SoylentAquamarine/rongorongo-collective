#!/usr/bin/env python3
"""Synthetic round-trip check of SQ-2's four-field atlas schema
(original_glyph_id, mapped_value, uncertain_flag, empty_mapping_flag),
per ChatGPT's proposed next step (comms/FromChatGPTToClaude.md Round 2).

Uses only synthetic rows for the three Barthel IDs already pinned by
ChatGPT's direct byte-level read of rongopy's horley_encoding.py (Round 1):
'17' -> '17', '18' -> '17' (many-to-one collapse), '199' -> '' (empty
mapping). No corpus-content data is read or required -- this tests the
SCHEMA's losslessness, not any actual corpus row.

Usage:
    python data/scripts/sq2_schema_roundtrip_check.py
"""

from __future__ import annotations

# The exact three cases ChatGPT's Round 1 byte-level read confirmed exist in
# horley_encoding.py: two Barthel IDs collapsing to one Horley value, and one
# empty-output case.
SYNTHETIC_ROWS = [
    {"original_glyph_id": "17", "mapped_value": "17"},
    {"original_glyph_id": "18", "mapped_value": "17"},
    {"original_glyph_id": "199", "mapped_value": ""},
]


def build_schema_rows(raw_rows: list[dict]) -> list[dict]:
    """Applies the four-field schema (config/sidequests.md SQ-2)."""
    out = []
    for row in raw_rows:
        out.append({
            "original_glyph_id": row["original_glyph_id"],
            "mapped_value": row["mapped_value"],
            "uncertain_flag": "?" in row["mapped_value"],
            "empty_mapping_flag": row["mapped_value"] == "",
        })
    return out


def check_lossless_roundtrip(schema_rows: list[dict]) -> dict:
    """Confirms every original_glyph_id can be recovered uniquely, even
    where mapped_value collapses two different originals to one value."""
    recovered_ids = {row["original_glyph_id"] for row in schema_rows}
    expected_ids = {row["original_glyph_id"] for row in SYNTHETIC_ROWS}
    lossless = recovered_ids == expected_ids

    by_mapped_value: dict[str, list[str]] = {}
    for row in schema_rows:
        by_mapped_value.setdefault(row["mapped_value"], []).append(row["original_glyph_id"])
    many_to_one_cases = {k: v for k, v in by_mapped_value.items() if len(v) > 1}

    empty_cases = [row["original_glyph_id"] for row in schema_rows if row["empty_mapping_flag"]]

    return {
        "lossless_roundtrip": lossless,
        "recovered_ids": sorted(recovered_ids),
        "many_to_one_cases": many_to_one_cases,
        "empty_mapping_cases": empty_cases,
    }


def main() -> None:
    schema_rows = build_schema_rows(SYNTHETIC_ROWS)
    result = check_lossless_roundtrip(schema_rows)

    for row in schema_rows:
        print(row)
    print()
    print(f"lossless_roundtrip: {result['lossless_roundtrip']}")
    print(f"many_to_one_cases (mapped_value -> [original_glyph_ids]): {result['many_to_one_cases']}")
    print(f"empty_mapping_cases (original_glyph_ids): {result['empty_mapping_cases']}")

    assert result["lossless_roundtrip"], "schema failed to preserve original IDs"
    assert result["many_to_one_cases"] == {"17": ["17", "18"]}, "17/18 collapse case not reproduced"
    assert result["empty_mapping_cases"] == ["199"], "199 empty-mapping case not reproduced"
    print("\nAll assertions passed: the four-field schema is lossless for these three pinned cases.")


if __name__ == "__main__":
    main()
