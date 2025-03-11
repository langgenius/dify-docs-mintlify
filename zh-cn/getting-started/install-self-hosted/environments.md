# 环境变量说明

### 公共变量

#### CONSOLE\_API\_URL

控制台 API 后端 URL，用于拼接授权回调，传空则为同域。范例：`https://api.console.dify.ai`。

#### CONSOLE\_WEB\_URL

控制台 web **前端** URL，用于拼接部分前端地址，以及 CORS 配置使用，传空则为同域。范例：`https://console.dify.ai`

#### SERVICE\_API\_URL

Service API URL，用于 **前端** 展示 Service API Base URL，传空则为同域。范例：`https://api.dify.ai`

#### APP\_API\_URL

WebApp API 后端 URL，用于声明 **前端** API 后端地址，传空则为同域。范例：`https://app.dify.ai`

#### APP\_WEB\_URL

WebApp URL，用于预览文件、**前端** 展示下载用的 URL，以及作为多模型输入接口，传空则为同域。范例：`https://udify.app/`

#### FILES\_URL

文件预览或下载 URL 前缀，用于将文件预览或下载 URL 给前端展示或作为多模态模型输入； 为了防止他人伪造，图片预览 URL 是带有签名的，并且有 5 分钟过期时间。

***

### 服务端

#### MODE

启动模式，仅使用 Docker 启动时可用，源码启动无效。

*   api

    启动 API Server。
*   worker

    启动异步队列 worker。

#### DEBUG

调试模式，默认 false，建议本地开发打开该配置，可防止 monkey patch 导致的一些问题出现。

#### FLASK\_DEBUG

Flask 调试模式，开启可在接口输出 trace 信息，方便调试。

#### SECRET\_KEY

一个用于安全地签名会话 cookie 并在数据库上加密敏感信息的密钥。初次启动需要设置改变量。可以运行 `openssl rand -base64 42` 生成一个强密钥。

#### DEPLOY\_ENV

部署环境。

*   PRODUCTION（默认）

    生产环境。
*   TESTING

    测试环境，前端页面会有明显颜色标识，该环境为测试环境。

#### LOG\_LEVEL

日志输出等级，默认为 INFO。生产建议设置为 ERROR。

#### MIGRATION\_ENABLED

当设置为 true 时，会在容器启动时自动执行数据库迁移，仅使用 Docker 启动时可用，源码启动无效。源码启动需要在 api 目录手动执行 `flask db upgrade`。

#### CHECK\_UPDATE\_URL

是否开启检查版本策略，若设置为 false，则不调用 `https://updates.dify.ai` 进行版本检查。由于目前国内无法直接访问基于 CloudFlare Worker 的版本接口，设置该变量为空，可以屏蔽该接口调用。

#### TEXT\_GENERATION\_TIMEOUT\_MS

默认 60000，单位为 ms，用于指定文本生成和工作流的超时时间，防止因某些进程运行超时而导致整体服务不可用。

#### CSP_WHITELIST

内容安全策略（CSP）白名单，默认不开启。在此变量中填写被放行的域名列表后即视为开启，有助于减少潜在的 XSS 攻击。开启后，白名单将自动包含以下域名：

```url
*.sentry.io http://localhost:* http://127.0.0.1:* https://analytics.google.com https://googletagmanager.com https://api.github.com
```

#### 容器启动相关配置

仅在使用 Docker 镜像或者 Docker-compose 启动时有效。

*   DIFY\_BIND\_ADDRESS

    API 服务绑定地址，默认：0.0.0.0，即所有地址均可访问。
*   DIFY\_PORT

    API 服务绑定端口号，默认 5001。
*   SERVER\_WORKER\_AMOUNT

    API 服务 Server worker 数量，即 gevent worker 数量，公式：`cpu 核心数 x 2 + 1` 可参考：https://docs.gunicorn.org/en/stable/design.html#how-many-workers
*   SERVER\_WORKER\_CLASS

    默认为 gevent，若为 windows，可以切换为 sync 或 solo。
*   GUNICORN\_TIMEOUT

    请求处理超时时间，默认 200，建议 360，以支持更长的 sse 连接时间。
*   CELERY\_WORKER\_CLASS

    和 `SERVER_WORKER_CLASS` 类似，默认 gevent，若为 windows，可以切换为 sync 或 solo。
*   CELERY\_WORKER\_AMOUNT

    Celery worker 数量，默认为 1，按需设置。
*   HTTP\_PROXY

    HTTP 代理地址，用于解决国内无法访问 OpenAI、HuggingFace 的问题。注意，若代理部署在宿主机 (例如 `http://127.0.0.1:7890`)，此处代理地址应当和接入本地模型时一样，使用 Docker 容器内部的宿主机地址（例如 `http://192.168.1.100:7890` 或 `http://172.17.0.1:7890`）。
*   HTTPS\_PROXY

    HTTPS 代理地址，用于解决国内无法访问 OpenAI、HuggingFace 的问题。同上。

#### 数据库配置

数据库使用 PostgreSQL，请使用 public schema。

* DB\_USERNAME：用户名
* DB\_PASSWORD：密码
* DB\_HOST：数据库 host
* DB\_PORT：数据库端口号，默认 5432
* DB\_DATABASE：数据库 database
* SQLALCHEMY\_POOL\_SIZE：数据库连接池大小，默认 30 个连接数，可适当增加。
* SQLALCHEMY\_POOL\_RECYCLE：数据库连接池回收时间，默认 3600 秒。
* SQLALCHEMY\_ECHO：是否打印 SQL，默认 false。

#### Redis 配置

该 Redis 配置用于缓存以及对话时的 pub/sub。

* REDIS\_HOST：Redis host
* REDIS\_PORT：Redis port，默认 6379
* REDIS\_DB：Redis Database，默认为 0，请和 Session Redis、Celery Broker 分开用不同 Database。
* REDIS\_USERNAME：Redis 用户名，默认为空
* REDIS\_PASSWORD：Redis 密码，默认为空，强烈建议设置密码。
* REDIS\_USE\_SSL：是否使用 SSL 协议进行连接，默认 false
* REDIS\_USE\_SENTINEL：使用 Redis Sentinel 连接 Redis 服务器
* REDIS\_SENTINELS：哨兵节点，格式：`<sentinel1_ip>:<sentinel1_port>,<sentinel2_ip>:<sentinel2_port>,<sentinel3_ip>:<sentinel3_port>`
* REDIS\_SENTINEL\_SERVICE\_NAME：哨兵服务名，同 Master Name
* REDIS\_SENTINEL\_USERNAME：哨兵的用户名
* REDIS\_SENTINEL\_PASSWORD：哨兵的密码
* REDIS\_SENTINEL\_SOCKET\_TIMEOUT：哨兵超时时间，默认值：0.1，单位：秒

#### Celery 配置

*   CELERY\_BROKER\_URL

    格式如下（直连模式）：

    ```
    redis://<redis_username>:<redis_password>@<redis_host>:<redis_port>/<redis_database>
  ```

    范例：`redis://:difyai123456@redis:6379/1`

    哨兵模式：

    ```
      sentinel://<sentinel_username>:<sentinel_password>@<sentinel_host>:<sentinel_port>/<redis_database>
  ```

    范例：`sentinel://localhost:26379/1;sentinel://localhost:26380/1;sentinel://localhost:26381/1`
    
*   BROKER\_USE\_SSL

    若设置为 true，则使用 SSL 协议进行连接，默认 false。

*   CELERY\_USE\_SENTINEL

    若设置为 true，则启用哨兵模式，默认 false。

*   CELERY_SENTINEL_MASTER_NAME

    哨兵的服务名，即 Master Name。

*   CELERY_SENTINEL_SOCKET_TIMEOUT

    哨兵连接超时时间，默认值：0.1，单位：秒。

#### CORS 配置

用于设置前端跨域访问策略。

*   CONSOLE\_CORS\_ALLOW\_ORIGINS

    控制台 CORS 跨域策略，默认为 `*`，即所有域名均可访问。
*   WEB\_API\_CORS\_ALLOW\_ORIGINS

    WebAPP CORS 跨域策略，默认为 `*`，即所有域名均可访问。

详细配置可参考：[跨域 / 身份相关指南](https://docs.dify.ai/v/zh-hans/learn-more/faq/install-faq#id-3.-an-zhuang-shi-hou-wu-fa-deng-lu-deng-lu-cheng-gong-dan-hou-xu-jie-kou-jun-ti-shi-401)

#### 文件存储配置

用于存储知识库上传的文件、团队 / 租户的加密密钥等等文件。

*   STORAGE\_TYPE

    存储设施类型

    *   local（默认）

        本地文件存储，若选择此项则需要设置下方 `STORAGE_LOCAL_PATH` 配置。
    *   s3

        S3 对象存储，若选择此项则需要设置下方 S3\_ 开头的配置。
    *   azure-blob

        Azure Blob 存储，若选择此项则需要设置下方 AZURE\_BLOB\_ 开头的配置。
    *   huawei-obs

        Huawei OBS 存储，若选择此项则需要设置下方 HUAWEI\_OBS\_ 开头的配置。
    *   volcengine-tos

        Volcengine TOS 存储，若选择此项则需要设置下方 VOLCENGINE\_TOS\_ 开头的配置。
*   STORAGE\_LOCAL\_PATH

    默认为 storage，即存储在当前目录的 storage 目录下。若使用 Docker 或 Docker-compose 进行部署，请务必将两个容器中 `/app/api/storage` 目录挂载到同一个本机目录，否则可能会出现文件找不到的报错。
* S3\_ENDPOINT：S3 端点地址
* S3\_BUCKET\_NAME：S3 桶名称
* S3\_ACCESS\_KEY：S3 Access Key
* S3\_SECRET\_KEY：S3 Secret Key
* S3\_REGION：S3 地域信息，如：us-east-1
* AZURE\_BLOB\_ACCOUNT\_NAME: your-account-name 如 'difyai'
* AZURE\_BLOB\_ACCOUNT\_KEY: your-account-key 如 'difyai'
* AZURE\_BLOB\_CONTAINER\_NAME: your-container-name 如 'difyai-container'
* AZURE\_BLOB\_ACCOUNT\_URL: 'https://\<your\_account\_name>.blob.core.windows.net'
* ALIYUN\_OSS\_BUCKET_NAME: your-bucket-name 如 'difyai'
* ALIYUN\_OSS\_ACCESS_KEY: your-access-key 如 'difyai'
* ALIYUN\_OSS\_SECRET_KEY: your-secret-key 如 'difyai'
* ALIYUN\_OSS\_ENDPOINT: https://oss-ap-southeast-1-internal.aliyuncs.com # 参考[文档](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints)
* ALIYUN\_OSS\_REGION: ap-southeast-1 # 参考[文档](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints)
* ALIYUN\_OSS\_AUTH_VERSION: v4
* ALIYUN\_OSS\_PATH: your-path # 路径不要使用斜线 "/" 开头，阿里云 OSS 不支持。参考[文档](https://api.aliyun.com/troubleshoot?q=0016-00000005)
* HUAWEI\_OBS\_BUCKET\_NAME: your-bucket-name 如 'difyai'
* HUAWEI\_OBS\_SECRET\_KEY: your-secret-key 如 'difyai'
* HUAWEI\_OBS\_ACCESS\_KEY: your-access-key 如 'difyai'
* HUAWEI\_OBS\_SERVER: your-server-url # 参考[文档](https://support.huaweicloud.com/sdk-python-devg-obs/obs_22_0500.html)。
* VOLCENGINE_TOS_BUCKET_NAME: your-bucket-name 如 'difyai'。
* VOLCENGINE_TOS_SECRET_KEY: your-secret-key 如 'difyai'。
* VOLCENGINE_TOS_ACCESS_KEY: your-access-key 如 'difyai'。
* VOLCENGINE_TOS_REGION: your-region 如 'cn-guangzhou' # 参考[文档]( https://www.volcengine.com/docs/6349/107356)。
* VOLCENGINE_TOS_ENDPOINT: your-endpoint 如 'tos-cn-guangzhou.volces.com' # 参考[文档](https://www.volcengine.com/docs/6349/107356)。

#### 向量数据库配置

*   VECTOR\_STORE

    **可使用的枚举类型包括：**

    * `weaviate`
    * `qdrant`
    * `milvus`
    * `zilliz` 与 `milvus` 一致
    * `myscale`
    * `pinecone` (暂未开放)
    * `tidb_vector`
    * `analyticdb`
    * `couchbase`
*   WEAVIATE\_ENDPOINT

    Weaviate 端点地址，如：`http://weaviate:8080`。
*   WEAVIATE\_API\_KEY

    连接 Weaviate 使用的 api-key 凭据。
*   WEAVIATE\_BATCH\_SIZE

    Weaviate 批量创建索引 Object 的数量，默认 100。可参考此[文档](https://weaviate.io/developers/weaviate/manage-data/import#how-to-set-batch-parameters)。
*   WEAVIATE\_GRPC\_ENABLED

    是否使用 gRPC 方式与 Weaviate 进行交互，开启后性能会大大增加，本地可能无法使用，默认为 true。
*   QDRANT\_URL

    Qdrant 端点地址，如：`https://your-qdrant-cluster-url.qdrant.tech/`
*   QDRANT\_API\_KEY

    连接 Qdrant 使用的 api-key 凭据。
*   PINECONE\_API\_KEY

    连接 Pinecone 使用的 api-key 凭据。
*   PINECONE\_ENVIRONMENT

    Pinecone 所在的额环境，如：`us-east4-gcp`
*   MILVUS\_URI

    Milvus 的 URI 配置。例如：`http://host.docker.internal:19530`。对于 [Zilliz Cloud](https://docs.zilliz.com.cn/docs/free-trials)，请将 URI 和 TOKEN 分别设置为 Public Endpoint 和 API Key。
*   MILVUS\_TOKEN

    Milvus TOKEN 配置，默认为空。
*   MILVUS\_USER

    Milvus 用户名配置，默认为空。
*   MILVUS\_PASSWORD

    Milvus 密码配置，默认为空。
*   MYSCALE\_HOST

    MyScale host 配置。
*   MYSCALE\_PORT

    MyScale port 配置。
*   MYSCALE\_USER

    MyScale 用户名配置，默认为 `default`。
*   MYSCALE\_PASSWORD

    MyScale 密码配置，默认为空。
*   MYSCALE\_DATABASE

    MyScale 数据库配置，默认为 `default`。
*   MYSCALE\_FTS\_PARAMS

    MyScale 全文搜索配置，如需多语言支持，请参考 [MyScale 文档](https://myscale.com/docs/en/text-search/#understanding-fts-index-parameters)，默认为空（仅支持英语）。

* TIDB\_VECTOR\_HOST

  TiDB Vector host 配置，如：`xxx.eu-central-1.xxx.tidbcloud.com`
* TIDB\_VECTOR\_PORT

  TiDB Vector 端口号配置，如：`4000`
* TIDB\_VECTOR\_USER

  TiDB Vector 用户配置，如：`xxxxxx.root`
* TIDB\_VECTOR\_PASSWORD

  TiDB Vector 密码配置
* TIDB\_VECTOR\_DATABASE

  TiDB Vector 数据库配置，如：`dify`

*   ANALYTICDB_KEY_ID

    用于阿里云 OpenAPI 认证的访问密钥 ID。请阅读 [Analyticdb 文档](https://help.aliyun.com/zh/analyticdb/analyticdb-for-postgresql/support/create-an-accesskey-pair) 来创建你的 AccessKey。

*   ANALYTICDB_KEY_SECRET

    用于阿里云 OpenAPI 认证的访问密钥秘密。

*   ANALYTICDB_INSTANCE_ID

    你的 AnalyticDB 实例的唯一标识符，例如 `gp-xxxxxx`。请阅读 [Analyticdb 文档](https://help.aliyun.com/zh/analyticdb/analyticdb-for-postgresql/getting-started/create-an-instance-1) 来创建你的实例。

*   ANALYTICDB_REGION_ID

    AnalyticDB 实例所在区域的标识符，例如 `cn-hangzhou`。

*   ANALYTICDB_ACCOUNT

    用于连接 AnalyticDB 实例的账户名称。请阅读 [Analyticdb 文档](https://help.aliyun.com/zh/analyticdb/analyticdb-for-postgresql/getting-started/createa-a-privileged-account) 来创建账户。

*   ANALYTICDB_PASSWORD

    用于连接 AnalyticDB 实例的账户密码。

*   ANALYTICDB_NAMESPACE

    在 AnalyticDB 实例内要操作的命名空间 (schema)，例如 `dify`。如果此命名空间不存在，将自动创建。

*   ANALYTICDB_NAMESPACE_PASSWORD

    命名空间 (schema) 的密码。如果命名空间不存在，将使用此密码进行创建。

-   COUCHBASE_CONNECTION_STRING

    Couchbase 集群的连接 string 字符串。

-   COUCHBASE_USER

    数据库用户名。

-   COUCHBASE_PASSWORD

    数据库密码。

-   COUCHBASE_BUCKET_NAME

     Bucket 名称。

-   COUCHBASE_SCOPE_NAME

     Scope 名称。

#### 知识库配置

*   UPLOAD\_FILE\_SIZE\_LIMIT

    上传文件大小限制，默认 15M。
*   UPLOAD\_FILE\_BATCH\_LIMIT

    每次上传文件数上限，默认 5 个。
*   ETL\_TYPE

    **可使用的枚举类型包括：**

    *   dify

        Dify 自研文件 Extract 方案
    *   Unstructured

        Unstructured.io 文件 Extract 方案
*   UNSTRUCTURED\_API\_URL

    Unstructured API 路径，当 ETL\_TYPE 为 Unstructured 需要配置。

    如：`http://unstructured:8000/general/v0/general`

#### 多模态模型配置

*   MULTIMODAL\_SEND\_IMAGE\_FORMAT

    多模态模型输入时，发送图片的格式，默认为 `base64`，可选 `url`。 `url` 模式下，调用的延迟会比 `base64` 模式下低，一般建议使用兼容更好的 `base64` 模式。 若配置为 `url`，则需要将 `FILES_URL` 配置为外部可访问的地址，以便多模态模型可以访问到图片。
*   UPLOAD\_IMAGE\_FILE\_SIZE\_LIMIT

    上传图片文件大小限制，默认 10M。

#### Sentry 配置

用于应用监控和错误日志跟踪。

*   SENTRY\_DSN

    Sentry DSN 地址，默认为空，为空时则所有监控信息均不上报 Sentry。
*   SENTRY\_TRACES\_SAMPLE\_RATE

    Sentry events 的上报比例，若为 0.01，则为 1%。
*   SENTRY\_PROFILES\_SAMPLE\_RATE

    Sentry profiles 的上报比例，若为 0.01，则为 1%。

#### Notion 集成配置

Notion 集成配置，变量可通过申请 Notion integration 获取：[https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)

* NOTION\_CLIENT\_ID
* NOTION\_CLIENT\_SECRET

#### 邮件相关配置

* MAIL\_TYPE
  * resend
    * MAIL\_DEFAULT\_SEND\_FROM\
      发件人的电子邮件名称，例如：no-reply [no-reply@dify.ai](mailto:no-reply@dify.ai)，非必需。
    * RESEND\_API\_KEY\
      用于 Resend 邮件提供程序的 API 密钥，可以从 API 密钥获取。
  * smtp
    * SMTP\_SERVER\
      SMTP 服务器地址
    * SMTP\_PORT\
      SMTP 服务器端口号
    * SMTP\_USERNAME\
      SMTP 用户名
    * SMTP\_PASSWORD\
      SMTP 密码
    * SMTP\_USE\_TLS\
      是否使用 TLS，默认为 false
    * MAIL\_DEFAULT\_SEND\_FROM\
      发件人的电子邮件名称，例如：no-reply [no-reply@dify.ai](mailto:no-reply@dify.ai)，非必需。

#### 模型供应商 & 工具 位置配置

用于指定应用中可以使用的模型供应商和工具。你可以自定义哪些工具和模型供应商可用，以及它们在应用界面中的顺序和包含 / 排除情况。

详见可用的 [工具](https://github.com/langgenius/dify/blob/main/api/core/tools/provider/_position.yaml) 和 [模型供应商](https://github.com/langgenius/dify/blob/main/api/core/model_runtime/model_providers/_position.yaml)。

* POSITION_TOOL_PINS

    将列出的工具固定在列表顶部，确保它们在界面中置顶出现。（使用逗号分隔的值，**中间不留空格**。）

    示例: `POSITION_TOOL_PINS=bing,google`

* POSITION_TOOL_INCLUDES

    指定要在应用中包含的工具。只有此处列出的工具才可用。如果未设置，则除非在 POSITION_TOOL_EXCLUDES 中指定，否则所有工具都会包含在内。（使用逗号分隔的值，**中间不留空格**。）

    示例: `POSITION_TOOL_INCLUDES=bing,google`

* POSITION_TOOL_EXCLUDES

    排除在应用中显示或使用的特定工具。此处列出的工具将从可用选项中省略，除非它们被固定。（使用逗号分隔的值，**中间不留空格**。）

    示例: `POSITION_TOOL_EXCLUDES=yahoo,wolframalpha`

* POSITION_PROVIDER_PINS

    将列出的模型供应商固定在列表顶部，确保它们在界面中置顶出现。（使用逗号分隔的值，**中间不留空格**。）

    示例: `POSITION_PROVIDER_PINS=openai,openllm`

* POSITION_PROVIDER_INCLUDES

    指定要在应用中包含的模型供应商。只有此处列出的供应商才可用。如果未设置，则除非在 POSITION_PROVIDER_EXCLUDES 中指定，否则所有供应商都会包含在内。（使用逗号分隔的值，**中间不留空格**。）

    示例: `POSITION_PROVIDER_INCLUDES=cohere,upstage`

* POSITION_PROVIDER_EXCLUDES

    排除在应用中显示特定模型供应商。此处列出的供应商将从可用选项中移除，除非它们被置顶。（使用逗号分隔的值，**中间不留空格**。）

    示例: `POSITION_PROVIDER_EXCLUDES=openrouter,ollama`

#### 其他

* INVITE\_EXPIRY\_HOURS：成员邀请链接有效时间（小时），默认：72。
* HTTP\_REQUEST\_NODE_MAX\_TEXT\_SIZE：workflow 工作流中 HTTP 请求节点的最大文本大小，默认 1MB。
* HTTP\_REQUEST\_NODE\_MAX\_BINARY\_SIZE：workflow 工作流中 HTTP 请求节点的最大二进制大小，默认 10MB。

***

### Web 前端

#### SENTRY\_DSN

Sentry DSN 地址，默认为空，为空时则所有监控信息均不上报 Sentry。

## 已废弃

#### CONSOLE\_URL

> ⚠️ 修改于 0.3.8，于 0.4.9 废弃，替代为：`CONSOLE_API_URL` 和 `CONSOLE_WEB_URL`。

控制台 URL，用于拼接授权回调、控制台前端地址，以及 CORS 配置使用，传空则为同域。范例：`https://console.dify.ai`。

#### API\_URL

> ⚠️ 修改于 0.3.8，于 0.4.9 废弃，替代为 `SERVICE_API_URL`。

API Url，用于给前端展示 Service API Base Url，传空则为同域。范例：`https://api.dify.ai`

#### APP\_URL

> ⚠️ 修改于 0.3.8，于 0.4.9 废弃，替代为 `APP_API_URL` 和 `APP_WEB_URL`。

WebApp Url，用于显示文件预览或下载 URL 到前端作为多模型输入，传空则为同域。范例：`https://udify.app/`

#### Session 配置

> ⚠️ 该配置从 0.3.24 版本起废弃。

仅 API 服务使用，用于验证接口身份。

* SESSION\_TYPE： Session 组件类型
  *   redis（默认）

      选择此项，则需要设置下方 SESSION\_REDIS\_ 开头的环境变量。
  *   sqlalchemy

      选择此项，则使用当前数据库连接，并使用 sessions 表进行读写 session 记录。
* SESSION\_REDIS\_HOST：Redis host
* SESSION\_REDIS\_PORT：Redis port，默认 6379
* SESSION\_REDIS\_DB：Redis Database，默认为 0，请和 Redis、Celery Broker 分开用不同 Database。
* SESSION\_REDIS\_USERNAME：Redis 用户名，默认为空
* SESSION\_REDIS\_PASSWORD：Redis 密码，默认为空，强烈建议设置密码。
* SESSION\_REDIS\_USE\_SSL：是否使用 SSL 协议进行连接，默认 false

#### Cookie 策略配置

> ⚠️ 该配置从 0.3.24 版本起废弃。

用于设置身份校验的 Session Cookie 浏览器策略。

*   COOKIE\_HTTPONLY

    Cookie HttpOnly 配置，默认为 true。
*   COOKIE\_SAMESITE

    Cookie SameSite 配置，默认为 Lax。
*   COOKIE\_SECURE

    Cookie Secure 配置，默认为 false。

### 文档分段长度配置

#### MAXIMUM_CHUNK_TOKEN_LENGTH 

文档分段长度配置，用于控制处理长文本时的分段大小。默认值：500。最大值：4000。

**较大分段**
- 可在单个分段内保留更多上下文，适合需要处理复杂或上下文相关任务的场景。
- 分段数量减少，从而降低处理时间和存储需求。

**较小分段**
- 提供更高的粒度，适合精确提取或总结文本内容。
- 减少超出模型 token 限制的风险，更适配限制严格的模型。

**配置建议**
- 较大分段：适合上下文依赖性强的任务，例如情感分析或长文档总结。
- 较小分段：适合精细分析场景，例如关键词提取或段落级内容处理。
