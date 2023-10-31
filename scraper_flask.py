from flask import Flask, request, jsonify
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# Download the NLTK stopwords and punkt datasets
nltk.download('stopwords')
nltk.download('punkt')

technical_terms = [
    # Programming Languages
    "Python", "Java", "C++", "JavaScript", "Ruby", "C#", "Swift", "Go (Golang)", "Go", "Kotlin", "PHP", "R", "MATLAB", "Lua", "Groovy", "Dart", "Objective-C", "Julia", "Cobol", "Assembly Language", "VHDL", "Verilog", "Fortran", "Ada", "Lisp", "Prolog",

    # Web Development Frameworks
    "React", "Angular", "Vue.js", "Django", "Ruby on Rails", "Laravel", "Flask", "Spring Framework", "Express.js", "ASP.NET", "Node.js", "Meteor", "Ember.js", "Backbone.js",

    # Java Web Frameworks
    "Spring Framework", "Spring Boot", "JavaServer Faces (JSF)", "Apache Struts", "Play Framework", "Grails",

    # Node.js Frameworks
    "Express.js", "NestJS", "Sails.js", "Koa.js", "Meteor", "AdonisJS", "LoopBack",

    # Golang Web Frameworks
    "Gin", "Echo", "Fiber", "Beego", "Revel", "Iris", "Buffalo",

    # Python Frameworks
    "Django", "Flask", "Pyramid", "FastAPI", "Tornado", "Bottle", "CherryPy", "Web2py", "TurboGears", "Falcon", "Quart",

    # Messaging Queues
    "RabbitMQ", "Apache Kafka", "ActiveMQ", "NATS", "ZeroMQ", "MQTT", "RabbitMQ",

    # RPC Frameworks
    "gRPC", "Apache Thrift", "Protocol Buffers", "JSON-RPC", "XML-RPC", "CORBA",

    # RPC Frameworks for Specific Languages
    "Pyro (Python)", "RPyC (Python)", "Java RMI (Java Remote Method Invocation)", "Hessian (Java)", "Burlap (Java)", "gRPC-Java (Java)", "NATS-RPC (Golang)", "gRPC-Golang (Golang)",

    # Mobile App Development Frameworks
    "React Native", "Flutter", "Xamarin", "NativeScript", "PhoneGap (Apache Cordova)", "Ionic", "Swift (for iOS development)", "Kotlin (for Android development)",

    # Database Systems
    "MySQL", "PostgreSQL", "SQLite", "MongoDB", "Oracle", "SQL Server", "Redis", "Cassandra", "MariaDB", "Couchbase", "Amazon DynamoDB", "Neo4j", "Firebase Realtime Database",

    # Big Data and Data Analysis
    "Hadoop", "Spark", "Kafka", "Flink", "Hive", "Pig", "HBase", "Impala", "Solr", "Elasticsearch", "Tableau", "Power BI", "D3.js",

    # DevOps and Cloud Technologies
    "Docker", "Kubernetes (K8s)", "Jenkins", "Ansible", "Terraform", "Puppet", "Chef", "Vagrant", "AWS (Amazon Web Services)", "Azure (Microsoft Azure)", "Google Cloud Platform (GCP)", "OpenStack", "Docker Swarm", "Rancher", "OpenShift", "CircleCI", "Travis CI", "Heroku", "DigitalOcean", "Linode",

    # Version Control
    "Git", "Subversion (SVN)", "Mercurial",

    # Front-End Technologies
    "HTML", "CSS", "JavaScript", "TypeScript", "HTML5", "CSS3", "jQuery", "Bootstrap", "SASS/SCSS", "LESS", "Webpack", "Babel", "Vue.js", "React", "Angular", "Redux", "Material-UI",

    # AI and Machine Learning
    "TensorFlow", "PyTorch", "Scikit-Learn", "Keras", "OpenCV", "NLTK", "Pandas", "NumPy", "SciPy", "Matplotlib", "Gensim", "XGBoost", "H2O.ai", "Theano", "Deeplearning4j", "Reinforcement Learning", "Natural Language Processing (NLP)", "Computer Vision", "Generative Adversarial Networks (GANs)", "Convolutional Neural Networks (CNNs)", "Recurrent Neural Networks (RNNs)", "Long Short-Term Memory (LSTM)", "Transfer Learning", "AutoML", "Reinforcement Learning", "Deep Q-Networks (DQNs)",

    # Data Science and Data Analysis
    "Data Warehousing", "ETL (Extract, Transform, Load) Processes", "Data Lakes", "Business Intelligence", "Data Mining", "Predictive Analytics", "Time Series Analysis", "A/B Testing", "Data Visualization",

    # Databases and NoSQL
    "CouchDB", "OrientDB", "Riak", "InfluxDB", "ArangoDB", "Apache Cassandra", "Couchbase", "Amazon Redshift",

    # Security
    "Cybersecurity", "Penetration Testing", "Encryption", "Firewalls", "Intrusion Detection Systems (IDS)", "Intrusion Prevention Systems (IPS)", "Security Information and Event Management (SIEM)", "Ethical Hacking",

    # Networking
    "TCP/IP", "DNS (Domain Name System)", "DHCP (Dynamic Host Configuration Protocol)", "Load Balancing", "VPN (Virtual Private Network)", "Subnetting", "IPv4 and IPv6",

    # Cloud Computing Services
    "Amazon Web Services (AWS) Services", "Google Cloud Platform (GCP) Services", "Microsoft Azure Services", "Heroku", "DigitalOcean", "Alibaba Cloud", "Oracle Cloud", "IBM Cloud",
]

# Convert technical terms to lowercase
technical_terms = [term.lower() for term in technical_terms]


@app.route('/api/v1/extractor/analyse', methods=['POST'])
def extract_technical_terms():
    # Get the input text from the POST request
    data = request.json
    input_text = data.get('text', '')

    # Tokenize the input text
    words = word_tokenize(input_text)

    # Filter out common English stopwords and non-technical terms
    filtered_words = [word for word in words if word.lower() not in stopwords.words(
        'english') and word.lower() in technical_terms]

    # Filter out duplicates
    filtered_words = list(set(filtered_words))

    # Return the extracted technical terms as a JSON response
    return jsonify({"technical_terms": filtered_words})


if __name__ == '__main__':
    app.run(debug=True)
