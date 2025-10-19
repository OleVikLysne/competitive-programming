import subprocess
import os
import sys
import difflib
from pathlib import Path


def color_text(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "reset": "\033[0m",
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"

def run_tests(program_path: str, test_folder: str):
    test_folder = Path(test_folder)
    in_files = list(test_folder.glob("*.in"))

    if not in_files:
        print("No .in files found.")
        return

    total = len(in_files)
    passed = 0

    for in_file in in_files:
        ans_file = in_file.with_suffix(".ans")
        if not ans_file.exists():
            print(f"⚠️  Missing .ans file for {in_file.name}")
            continue

        try:
            with open(in_file, "r") as fin:
                result = subprocess.run(
                    [program_path],
                    stdin=fin,
                    capture_output=True,
                    text=True,
                    timeout=5,
                    shell=True,
                )
        except subprocess.TimeoutExpired:
            print(f"⏱️  {in_file.name} -> Timed out")
            continue
        except Exception as e:
            print(f"💥 Error running {in_file.name}: {e}")
            continue

        with open(ans_file, "r") as fans:
            expected_output = fans.read().strip()
        actual_output = result.stdout.strip()

        if actual_output == expected_output:
            print(f"✅ {in_file.stem} passed")
            passed += 1
        else:
            print(f"\n❌ {in_file.stem} failed")

            # Show line-by-line diff
            expected_lines = expected_output.splitlines()
            actual_lines = actual_output.splitlines()
            diff = difflib.ndiff(expected_lines, actual_lines)

            print(color_text("   Differences:", "yellow"))
            for line in diff:
                if line.startswith("-"):
                    print(color_text("   " + line, "red"))
                elif line.startswith("+"):
                    print(color_text("   " + line, "green"))
                elif line.startswith("?"):
                    continue  # skip markers
                else:
                    print("   " + line)
            print()  # blank line between tests

    print(f"\nSummary: {passed}/{total} tests passed.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python test_runner.py <program_path> <test_folder>")
        sys.exit(1)

    program = sys.argv[1]
    folder = sys.argv[2]
    run_tests(program, folder)
