import sys, importlib, json
print('PY_EXE:', sys.executable)
modules = ['streamlit','markdown','yaml','slugify','openai','requests']
for m in modules:
    try:
        mod = importlib.import_module(m)
        v = getattr(mod, '__version__', getattr(mod, 'VERSION', 'unknown'))
        print(f"{m}: OK ({v})")
    except Exception as e:
        print(f"{m}: IMPORT_ERROR -> {e}")

# Test local imports
try:
    import engine.generator as gen
    import engine.batch as batch
    import engine.utils as utils
    print('local imports: OK')
except Exception as e:
    print('local imports: ERROR ->', e)

# Dump wp config
try:
    from engine.utils import read_yaml
    cfg = read_yaml('config/wp_config.yaml')
    print('wp_config:', json.dumps(cfg or {}, indent=2))
except Exception as e:
    print('wp_config: ERROR ->', e)
