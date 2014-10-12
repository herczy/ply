#!/bin/bash

DESTPATH=test
if [ ! -d "$DESTPATH" ]
then
  mkdir -p "$DESTPATH"
fi

touch "$DESTPATH/__init__.py"

DEST="$DESTPATH/chartest_original.py"

cat >$DEST <<_EOF
from . import charbase


class TestOriginalChartests(charbase.PlyCharCase):
_EOF

i=0
for script in test/lex_*.py test/yacc_*.py
do
  i=$((i + 1))
  BASENAME=$(basename $script)
  SANITIZED_NAME=${BASENAME:0:-3}
  SANITIZED_NAME=$(echo -n $SANITIZED_NAME | tr -c '[a-zA-Z0-9_]' _)

  echo "$script => test_$SANITIZED_NAME"
  cat >>"$DEST" <<_EOF
    def test_$SANITIZED_NAME(self):
        self._execute_file("$BASENAME")

_EOF
done
