from fabric.api import run, env

env.use_ssh_config = True


def install_git():
	run("""sudo apt-get install -y git-core""")

def install_mongodb():
	#https://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/
	run("""sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10""")
	run("""echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list""")
	run("""sudo apt-get update""")
	run("""sudo apt-get install -y mongodb-org""")

def install_nodejs():
	#https://github.com/nodesource/distributions
	run("""curl -sL https://deb.nodesource.com/setup | sudo bash -""")
	run("""sudo apt-get update""")
	run("""sudo apt-get install -y nodejs""")

def install_compiler():
	run("""sudo apt-get install -y make g++""")

def install_gulp():
	run("""sudo npm install -g gulp""")

def install_bower():
	run("""sudo npm install -g bower""")

def install_meancli():
	run("""sudo npm install -g mean-cli""")
	run("""sudo chown -R `whoami` ~/.npm""")

def initialise_app(app_name):
	run("""mean init %s""" % app_name)
	run("""cd %s && npm install""" % app_name)

def bootstrap():
	install_git()
	install_mongodb()
	install_nodejs()
	install_compiler()
	install_gulp()
	install_bower()
	install_meancli()
