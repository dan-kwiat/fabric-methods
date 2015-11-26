from fabric.api import run, env, local

env.use_ssh_config = True


def ssh_tunnel(remote_host='awshost'):
	local("""ssh -L 8080:localhost:3000 %s""" % remote_host)

def install_git():
	run("""sudo apt-get install -y git-core""")
	run("""sudo apt-get update""")

def install_compiler():
	run("""sudo apt-get install -y make g++""")
	run("""sudo apt-get update""")

def install_nodejs():
	#https://github.com/nodesource/distributions
	run("""curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -""")
	run("""sudo apt-get update""")
	run("""sudo apt-get install -y nodejs""")
	run("""sudo apt-get update""")

def install_mongodb():
	#https://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/
	run("""sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10""")
	run("""echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list""")
	run("""sudo apt-get update""")
	run("""sudo apt-get install -y mongodb-org""")
	run("""sudo apt-get update""")

def install_ruby():
	run("""sudo apt-get install -y ruby-full""")
	run("""sudo apt-get update""")

def install_bower():
	run("""sudo npm install -g bower""")

def install_grunt():
	run("""sudo npm install -g grunt-cli""")

def install_gulp():
	run("""sudo npm install -g gulp""")

def install_sass():
	run("""sudo gem install sass""")

def install_app(app_name='meanjs'):
	run("""git clone https://github.com/meanjs/mean.git /home/ubuntu/%s""" % app_name)
	run("""cd /home/ubuntu/%s && npm install""" % app_name)

def run_app(app_name='meanjs'):
	run("""cd /home/ubuntu/%s && grunt""" % app_name)


def bootstrap():
	install_git()
	install_compiler()
	install_nodejs()
	install_mongodb()
	install_ruby()
	install_bower()
	install_grunt()
	install_gulp()
	install_sass()
