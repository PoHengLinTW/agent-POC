# POC to use HF's agent `smolagents`

## Steps
1. install virtual environment

```bash
python3 -m venv ./.venv
```

2. manual enable virtual environment if it is not picking virtual environment automatically 

```bash
source ./.venv/bin/activate
```

3. install the dependencies

```bash
pip3 install -r requirement.txt
```

4. run the POC
```bash
python3 text_to_sql.py

# or

python3 log_anomly_agent.py
```

