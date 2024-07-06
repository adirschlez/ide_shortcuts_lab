from enum import Enum

"""
1) GO TO SETTINGS -> Plugins and install String Manipulation
2) first try: 
    2.1) select one of the enum attribute 
    2.2) press OPT + M
    2.3) select switch case (or press 4)
    2.4) select snake case (or press 3)
    2.5) undo your changes (we're going big!)
3) going for the gold:
    3.1) put your cursor before ActivityLogs
    3.2) double click and hold OPT button and press down arrow (while holding OPT)
    3.3) going down till the end of the enum
    3.4) press OPT + Shift + right arrow (select all the enum attributes)
    3.5) CMD + C (copy)
    3.6) OPT + M
    3.7) select switch case (or press 4)
    3.8) select snake case (or press 3)
    3.6) press END and then left arrow (or right arrow till the middel of the apostrophes)
    3.7) CMD + V (paste)
    3.8) OPT + Shift + left arrow (select inner text)
    3.9) OPT + M
    3.10) select switch case (or press 4)
    3.11) select kebab case (or press 5)
    3.12) press CMD + Shift + U (convert to lower case)
    3.13) press CMD + Shift + U (convert to upper case) 
"""
class AzureEntityType(Enum):
    ActivityLogs = ''
    VirtualMachine = ''
    VirtualMachineScaleSet = ''
    LoadBalancer = ''
    LoadBalancingRule = ''
    SqlServer = ''
    SqlDB = ''
    KubernetesCluster = ''
    KubernetesAgentPools = ''
    DataLakeAnalyticsAccount = ''
    StorageAccount = ''
    StorageAccountAccessKeys = ''
    FileShare = ''
    BlobContainer = ''
    Queue = ''
    Table = ''
    Tenant = ''
    RedisCache = ''
    Disk = ''
    DnsZone = ''
    DnsRecord = ''
    KeyVault = ''
    KeyFromKeyVault = ''
    SecretFromKeyVault = ''
    CertificateFromKeyVault = ''
    RecoveryServiceVault = ''
    ResourceGroup = ''
    WebApp = ''
    ApiConnection = ''
    AppServicePlan = ''
    ApplicationInsight = ''
    ApplicationGateway = ''
    AppGatewayHttpListener = ''
    AzureDatabricks = ''
    ActionGroups = ''
    B2CTenant = ''
    LogAnalyticsWorkspace = ''
    LogAnalyticsMacAddresses = ''
    LogicApp = ''
    MachineLearningServiceRegistry = ''
    MachineLearningServiceWorkspace = ''
    MachineLearningWebService = ''
    ManagedIdentity = ''
    NetworkSecurityRules = ''
    NetworkSecurityGroup = ''
    NetworkWatcher = ''
    RouteTable = ''
    SignalR = ''
    SynapseWorkspace = ''
    ApacheSparkPool = ''
    DedicatedSQLPool = ''
    VirtualNetwork = ''
    CosmosDBAccount = ''
    AnalysisServicesServer = ''
    AppService = ''
    ArcEnabledMachine = ''
    AutomationAccount = ''
    AvailabilitySet = ''
    Workbook = ''
    CommunicationService = ''
    VNGatewayConnection = ''
    EventHub = ''
    EventHubNamespace = ''
    FrontDoorCDNProfile = ''
    FrontDoorWAFPolicy = ''
    LocalNetworkGateway = ''
    Relay = ''
    WCFRelay = ''
    ServiceBusNamespace = ''
    SharedDashboard = ''
    FormRecognizer = ''
    PrivateEndpoint = ''
    NetworkInterface = ''
    SystemTopic = ''
    Solutions = ''
    VirtualNetworkGateway = ''
    PublicIPAddress = ''
    AvailabilityTest = ''
    SentinelIncident = ''
    SqlManagedInstance = ''
    Firewall = ''
    WebApplicationFirewallPolicy = ''
    ApiManagement = ''
    ContainerApp = ''
    ContainerGroup = ''
    ContainerRegistry = ''
    DataFactory = ''
    PostgreSQLFlexibleServer = ''
    PostgreSQLSingleServer = ''
    MySQLFlexibleServer = ''
    MySQLSingleServer = ''
    MariaDB = ''
    Subscription = ''
    RoleAssignment = ''
    ComputeSnapshot = ''
    NetAppAccount = ''
    NetAppVolume = ''