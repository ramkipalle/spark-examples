from airflow import DAG, utils
from ocean_spark.operators import (
    OceanSparkOperator,
)

args = {
    "owner": "airflow",
    "email": [],  # ["airflow@example.com"],
    "depends_on_past": False,
    "start_date": utils.dates.days_ago(0, second=1),
}


dag = DAG(dag_id="spark-ghcr-helloexample1", default_args=args, schedule_interval=None)

spark_pi_task = OceanSparkOperator(
    task_id="spark-ghcr-helloexample1",
    dag=dag,
    config_overrides={
        "type": "Python",
        "sparkVersion": "3.2.0",
        "imagePullSecrets": ["github-pull-image-secret"],
        "imagePullPolicy": "Always",
        "image": "ghcr.io/ramkipalle/spark-examples/helloexample1:latest",
        "mainApplicationFile": "local:///opt/application/HelloExample1.py",
        "driver": {
            "cores": 1,
            "instanceSelector":"m5",
        },
        "executor": {
            "cores": 4,
            "instanceSelector":"m5d",
            "instances": 1
        }
    }
)