import json,io,contextlib,os
from pathlib import Path
root=Path(__file__).resolve().parents[1]; os.chdir(root)
p=root/'notebooks/storm_scale.ipynb'; nb=json.loads(p.read_text()); ns={}; count=0
for cell in nb['cells']:
    if cell['cell_type']=='code':
        out=io.StringIO()
        with contextlib.redirect_stdout(out): exec(compile(''.join(cell['source']),str(p),'exec'),ns)
        count+=1; cell['execution_count']=count
        cell['outputs']=[{'name':'stdout','output_type':'stream','text':out.getvalue().splitlines(True)}]
        print(out.getvalue(),end='')
p.write_text(json.dumps(nb,indent=2,ensure_ascii=False)+'\n'); print(f'PASS: executed {count} notebook code cell(s) offline')
