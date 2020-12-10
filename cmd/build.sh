# Removes distribution files
bash cmd/rm.sh
# Stylizes code
black bd103
# Builds project
python3 setup.py sdist bdist_wheel