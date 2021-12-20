# Build documentation

SOURCEDIR=.
BUILDDIR=../docs
BUILDTYPE="$1"
CACHEDIR=_cache

if [ "$BUILDTYPE" = "" ]; then
    BUILDTYPE="html"
fi

poetry run sphinx-build -b $BUILDTYPE -d _cache -a $SOURCEDIR $BUILDDIR
