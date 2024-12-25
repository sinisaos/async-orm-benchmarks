Python async ORMs, query builders and drivers benchmarks.

---------------------------------------------------------

## Instalation

Clone repository in fresh virtualenv.

```bash
git clone https://github.com/sinisaos/async-orm-benchmarks.git
```

## Install requirements


```bash
cd async-orm-benchmarks/
pip install -r requirements.txt
```

## Create database


```bash
sudo -i -u yourpostgresusername psql
CREATE DATABASE perfdb;
\q;
```

## Create database tables and load data


```bash
./scripts/load_data.sh
```

## Usage

In the first terminal, start the `ORM` or `driver` server from the menu.

```bash
./scripts/start_server.sh
```

In the second terminal, run the benchmark (from the menu) for the server started in the first terminal.

```bash
./scripts/start_benchmark.sh
```

## Endpoints

This benchmarks attempts to simulate a realistic comparison of asynch ORMs and drivers. 
As in this [example case](https://github.com/edgedb/imdbench), we simulate the latency between the server and the database to get more realistic benchmarks.

On Linux, this latency can be simulated with `tc` tool like this:

```bash
sudo tc qdisc replace dev lo root netem delay 1ms
```

Once we finish our benchmark, it is important to delete the rule which we have set.

```bash
sudo tc qdisc delete dev lo root
```
----------------------
There are three types of tables. 

A small table with only two columns,

<details>
<summary>Multiple columns response</summary>

```json
[
   {
      "id":1,
      "name":"Tag 1"
   },
   {
      "id":2,
      "name":"Tag 2"
   },
   {
      "id":3,
      "name":"Tag 3"
   },
   {
      "id":4,
      "name":"Tag 4"
   },
   {
      "id":5,
      "name":"Tag 5"
   },
   {
      "id":6,
      "name":"Tag 6"
   },
   {
      "id":7,
      "name":"Tag 7"
   },
   "..."
]
```
</details>

<details>
<summary>Single column response</summary>

```json
{
    "id":1,
    "name":"Tag 1"
}
```
</details>

----------------------
A large table with many columns 


<details>
<summary>Multiple columns response</summary>

```json
[
   {
      "id":1,
      "float_col_1":2.2,
      "smallint_col_1":2,
      "integer_col_1":2000000,
      "bigint_col_1":99999999,
      "varchar_col_1":"value1",
      "text_col_1":"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
      "numeric_col_1":2.2,
      "json_col_1":{
         "a":1,
         "b":"b",
         "c":[
            2
         ],
         "d":{
            "e":3
         },
         "f":true
      },
      "float_col_2":2.2,
      "smallint_col_2":2,
      "integer_col_2":2000000,
      "bigint_col_2":99999999,
      "varchar_col_2":"value1",
      "text_col_2":"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
      "numeric_col_2":2.2,
      "json_col_2":{
         "a":1,
         "b":"b",
         "c":[
            2
         ],
         "d":{
            "e":3
         },
         "f":true
      },
      "float_col_3":2.2,
      "smallint_col_3":2,
      "integer_col_3":2000000,
      "bigint_col_3":99999999,
      "varchar_col_3":"value1",
      "text_col_3":"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
      "numeric_col_3":2.2,
      "json_col_3":{
         "a":1,
         "b":"b",
         "c":[
            2
         ],
         "d":{
            "e":3
         },
         "f":true
      }
   },
   {
      "id":2,
      "float_col_1":2.2,
      "smallint_col_1":2,
      "integer_col_1":2000000,
      "bigint_col_1":99999999,
      "varchar_col_1":"value1",
      "text_col_1":"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
      "numeric_col_1":2.2,
      "json_col_1":{
         "a":1,
         "b":"b",
         "c":[
            2
         ],
         "d":{
            "e":3
         },
         "f":true
      },
      "float_col_2":2.2,
      "smallint_col_2":2,
      "integer_col_2":2000000,
      "bigint_col_2":99999999,
      "varchar_col_2":"value1",
      "text_col_2":"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
      "numeric_col_2":2.2,
      "json_col_2":{
         "a":1,
         "b":"b",
         "c":[
            2
         ],
         "d":{
            "e":3
         },
         "f":true
      },
      "float_col_3":2.2,
      "smallint_col_3":2,
      "integer_col_3":2000000,
      "bigint_col_3":99999999,
      "varchar_col_3":"value1",
      "text_col_3":"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
      "numeric_col_3":2.2,
      "json_col_3":{
         "a":1,
         "b":"b",
         "c":[
            2
         ],
         "d":{
            "e":3
         },
         "f":true
      }
   },
   {
      "id":3,
      "float_col_1":2.2,
      "smallint_col_1":2,
      "integer_col_1":2000000,
      "bigint_col_1":99999999,
      "varchar_col_1":"value1",
      "text_col_1":"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
      "numeric_col_1":2.2,
      "json_col_1":{
         "a":1,
         "b":"b",
         "c":[
            2
         ],
         "d":{
            "e":3
         },
         "f":true
      },
      "float_col_2":2.2,
      "smallint_col_2":2,
      "integer_col_2":2000000,
      "bigint_col_2":99999999,
      "varchar_col_2":"value1",
      "text_col_2":"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
      "numeric_col_2":2.2,
      "json_col_2":{
         "a":1,
         "b":"b",
         "c":[
            2
         ],
         "d":{
            "e":3
         },
         "f":true
      },
      "float_col_3":2.2,
      "smallint_col_3":2,
      "integer_col_3":2000000,
      "bigint_col_3":99999999,
      "varchar_col_3":"value1",
      "text_col_3":"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
      "numeric_col_3":2.2,
      "json_col_3":{
         "a":1,
         "b":"b",
         "c":[
            2
         ],
         "d":{
            "e":3
         },
         "f":true
      }
   },
   {
      "id":4,
      "float_col_1":2.2,
      "smallint_col_1":2,
      "integer_col_1":2000000,
      "bigint_col_1":99999999,
      "varchar_col_1":"value1",
      "text_col_1":"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
      "numeric_col_1":2.2,
      "json_col_1":{
         "a":1,
         "b":"b",
         "c":[
            2
         ],
         "d":{
            "e":3
         },
         "f":true
      },
      "float_col_2":2.2,
      "smallint_col_2":2,
      "integer_col_2":2000000,
      "bigint_col_2":99999999,
      "varchar_col_2":"value1",
      "text_col_2":"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
      "numeric_col_2":2.2,
      "json_col_2":{
         "a":1,
         "b":"b",
         "c":[
            2
         ],
         "d":{
            "e":3
         },
         "f":true
      },
      "float_col_3":2.2,
      "smallint_col_3":2,
      "integer_col_3":2000000,
      "bigint_col_3":99999999,
      "varchar_col_3":"value1",
      "text_col_3":"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
      "numeric_col_3":2.2,
      "json_col_3":{
         "a":1,
         "b":"b",
         "c":[
            2
         ],
         "d":{
            "e":3
         },
         "f":true
      }
   },
   ...
]
```
</details>

<details>
<summary>Single column response</summary>

```json
{
    "id":1,
    "float_col_1":2.2,
    "smallint_col_1":2,
    "integer_col_1":2000000,
    "bigint_col_1":99999999,
    "varchar_col_1":"value1",
    "text_col_1":"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
    "numeric_col_1":2.2,
    "json_col_1":{
        "a":1,
        "b":"b",
        "c":[
        2
        ],
        "d":{
        "e":3
        },
        "f":true
    },
    "float_col_2":2.2,
    "smallint_col_2":2,
    "integer_col_2":2000000,
    "bigint_col_2":99999999,
    "varchar_col_2":"value1",
    "text_col_2":"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
    "numeric_col_2":2.2,
    "json_col_2":{
        "a":1,
        "b":"b",
        "c":[
        2
        ],
        "d":{
        "e":3
        },
        "f":true
    },
    "float_col_3":2.2,
    "smallint_col_3":2,
    "integer_col_3":2000000,
    "bigint_col_3":99999999,
    "varchar_col_3":"value1",
    "text_col_3":"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
    "numeric_col_3":2.2,
    "json_col_3":{
        "a":1,
        "b":"b",
        "c":[
        2
        ],
        "d":{
        "e":3
        },
        "f":true
    }
}
```
</details>

----------------------

and a related table that has multiple related tables (both `foreign key` and `many to many` relationships).

<details>
<summary>Multiple columns response</summary>

```json
[
   {
      "id":1,
      "title":"Question 1",
      "content":"Question 1",
      "created_at":"2024-12-02T05:30:23.101781+00:00",
      "updated_at":"2024-12-02T05:30:23.101801+00:00",
      "views":30529,
      "likes":10,
      "user_id":1,
      "question_user":{
         "id":1,
         "email":"piccolo@example.com",
         "username":"piccolo",
         "superuser":true
      },
      "question_tags":[
         {
            "id":14,
            "name":"Tag 14"
         },
         {
            "id":16,
            "name":"Tag 16"
         },
         {
            "id":22,
            "name":"Tag 22"
         }
      ]
   },
   {
      "id":2,
      "title":"Question 2",
      "content":"Question 2",
      "created_at":"2024-12-02T05:30:23.160412+00:00",
      "updated_at":"2024-12-02T05:30:23.160421+00:00",
      "views":10,
      "likes":10,
      "user_id":1,
      "question_user":{
         "id":1,
         "email":"piccolo@example.com",
         "username":"piccolo",
         "superuser":true
      },
      "question_tags":[
         {
            "id":16,
            "name":"Tag 16"
         },
         {
            "id":20,
            "name":"Tag 20"
         },
         {
            "id":21,
            "name":"Tag 21"
         }
      ]
   },
   {
      "id":3,
      "title":"Question 3",
      "content":"Question 3",
      "created_at":"2024-12-02T05:30:23.216031+00:00",
      "updated_at":"2024-12-02T05:30:23.216048+00:00",
      "views":10,
      "likes":10,
      "user_id":1,
      "question_user":{
         "id":1,
         "email":"piccolo@example.com",
         "username":"piccolo",
         "superuser":true
      },
      "question_tags":[
         {
            "id":11,
            "name":"Tag 11"
         },
         {
            "id":18,
            "name":"Tag 18"
         },
         {
            "id":19,
            "name":"Tag 19"
         }
      ]
   },
   {
      "id":4,
      "title":"Question 4",
      "content":"Question 4",
      "created_at":"2024-12-02T05:30:23.272343+00:00",
      "updated_at":"2024-12-02T05:30:23.272352+00:00",
      "views":10,
      "likes":10,
      "user_id":1,
      "question_user":{
         "id":1,
         "email":"piccolo@example.com",
         "username":"piccolo",
         "superuser":true
      },
      "question_tags":[
         {
            "id":4,
            "name":"Tag 4"
         },
         {
            "id":18,
            "name":"Tag 18"
         },
         {
            "id":22,
            "name":"Tag 22"
         }
      ]
   },
   {
      "id":5,
      "title":"Question 5",
      "content":"Question 5",
      "created_at":"2024-12-02T05:30:23.327549+00:00",
      "updated_at":"2024-12-02T05:30:23.327565+00:00",
      "views":10,
      "likes":10,
      "user_id":1,
      "question_user":{
         "id":1,
         "email":"piccolo@example.com",
         "username":"piccolo",
         "superuser":true
      },
      "question_tags":[
         {
            "id":1,
            "name":"Tag 1"
         },
         {
            "id":2,
            "name":"Tag 2"
         },
         {
            "id":9,
            "name":"Tag 9"
         },
         {
            "id":13,
            "name":"Tag 13"
         }
      ]
   },
   ...
]
```
</details>

<details>
<summary>Single column response</summary>

```json
{
   "id":1,
   "title":"Question 1",
   "content":"Question 1",
   "created_at":"2024-12-02T05:30:23.101781+00:00",
   "updated_at":"2024-12-02T05:30:23.101801+00:00",
   "views":30529,
   "likes":10,
   "user_id":1,
   "question_user":{
      "id":1,
      "email":"piccolo@example.com",
      "username":"piccolo",
      "superuser":true
   },
   "question_tags":[
      {
         "id":14,
         "name":"Tag 14"
      },
      {
         "id":16,
         "name":"Tag 16"
      },
      {
         "id":22,
         "name":"Tag 22"
      }
   ],
   "question_answers":[
      {
         "id":95,
         "content":"Answer 95",
         "created_at":"2024-12-02T06:30:46.201394+01:00",
         "updated_at":"2024-12-02T06:30:46.201403+01:00",
         "likes":20,
         "user_id":1,
         "question_id":1
      }
   ]
}
```
</details>

## Results

This benchmarks uses the [Bombardier](https://github.com/codesenberg/bombardier) load test tool with `200 connections` for `10 seconds` on `uvicorn` server with single worker. The results are in [results.md](https://github.com/sinisaos/async-orm-benchmarks/blob/main/results.md) and will be different on a better machine (I'm using an old machine with only `4GB RAM` and `Intel Core i3-6006U`). You can also use [Locust](https://locust.io/) for really nice GUI testing and reporting. PRs are welcome. Thanks in advance.