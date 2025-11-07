#!/bin/bash

# Generate HTML coverage report for the Griddy SDK
#
# Usage: ./scripts/coverage-report.sh
#
# This script runs pytest with coverage and generates an HTML report
# in the htmlcov/ directory. After running, open htmlcov/index.html
# in your browser to view the coverage report.

set -e

echo "Running unit tests with coverage..."
pytest -m unit --cov=src/griddy --cov-report=html --cov-report=term

echo ""
echo "✓ Coverage report generated successfully!"
echo ""
echo "To view the report, open: htmlcov/index.html"
echo ""
echo "  Example: xdg-open htmlcov/index.html  # Linux"
echo "           open htmlcov/index.html      # macOS"
echo "           start htmlcov/index.html     # Windows"
