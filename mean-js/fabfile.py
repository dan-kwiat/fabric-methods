from fabric.api import env, run, sudo, local

env.use_ssh_config = True


def ssh_tunnel(remote_host='awshost'):
	local("""ssh -L 8080:localhost:3000 %s""" % remote_host)

def install_git():
	sudo("""apt-get install -y git-core""")
	sudo("""apt-get update""")

def install_compiler():
	sudo("""apt-get install -y make g++""")
	sudo("""apt-get update""")

def install_nodejs():
	#https://github.com/nodesource/distributions
	run("""curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -""")
	sudo("""apt-get update""")
	sudo("""apt-get install -y nodejs""")
	sudo("""apt-get update""")

def install_mongodb():
	#https://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/
	sudo("""apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10""")
	run("""echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list""")
	sudo("""apt-get update""")
	sudo("""apt-get install -y mongodb-org""")
	sudo("""apt-get update""")

def install_ruby():
	sudo("""apt-get install -y ruby-full""")
	sudo("""apt-get update""")

def install_bower():
	sudo("""npm install -g bower""")

def install_grunt():
	sudo("""npm install -g grunt-cli""")

def install_gulp():
	sudo("""npm install -g gulp""")

def install_sass():
	sudo("""gem install sass""")

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
