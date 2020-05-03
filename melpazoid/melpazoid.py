"""Entrypoint to melpazoid."""
NO_COLOR = os.environ.get('NO_COLOR', False)
    if os.environ.get('EXIST_OK', '').lower() != 'true':
        print_related_packages(recipe)
    print(f"Building container for {_package_name(recipe)}... 🐳")
    if len([file for file in files if file.endswith('.el')]) > 1:
        main_file = os.path.basename(_main_file(files, recipe))
    else:
        main_file = ''  # no need to specify main file if it's the only file
        # NOTE: emacs --script <file.el> will set <file.el> to the load-file-name
        # which can disrupt the compilation of packages that check this:
        requirements_el.write('(let ((load-file-name nil))')
        requirements_el.write(') ; end let')
    reqs = sum((req.split('(')[1:] for req in reqs), [])
    for ii, req in enumerate(reqs):
        if '"' not in req:
            _fail(f"Version in '{req}' must be a string!  Attempting patch")
            package, version = reqs[ii].split()
            reqs[ii] = f'{package} "{version}"'
        if file.endswith('-pkg.el'):
            _note(f"- {file} -- consider excluding this; MELPA creates one", CLR_WARN)
            continue
        print(f"- {name}: {known_packages[name]}")
        _fail(f"- Error: a package called '{package_name}' exists", highlight='Error:')
def _local_repo() -> str:
        _fail(f"{pr_url} does not appear to be a MELPA PR: {pr_data}")
@functools.lru_cache()