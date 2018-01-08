1.

#!/bin/sh

python bigquery_test.py

2.

#!/bin/sh

python thread-api.py

2-2.

#!/bin/sh

python to_gcs.py

3.

#!/bin/sh

embulk run gcs_to_bigquery.yml

4.

#!/bin/sh

embulk run gcs_to_sql_pre.yml

5.

#!/bin/sh

embulk run gcs_to_sql_predict.yml
