#!/usr/bin/env python3
"""Warm Dinner — entry for Make the AI Judge Feel Proud: A Family Scene on make.fun.

Prints one short family scene (at most 280 characters): a small domestic
moment that is warm, funny and heartfelt.
"""

LINE = "Dad tried to fix the Wi-Fi by unplugging the fridge; dinner was warm, the ice cream was soup, and nobody reached for their phone."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 280
    print(LINE)


if __name__ == "__main__":
    main()
