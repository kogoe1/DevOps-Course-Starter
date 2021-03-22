# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below
Vagrant.configure("2") do |config|
 
  config.vm.box = "hashicorp/bionic64"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
   config.vm.network "forwarded_port", guest: 5000, host: 5000 

  # Enable provisioning with a shell script 
   config.vm.provision "shell", privileged: false, inline: <<-SHELL
     sudo apt-get update
     
     sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
       libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
       xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

    git clone https://github.com/pyenv/pyenv.git ~/.pyenv 
    
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.profile 

    # Enable environment variables  
    source ~/.profile

    # Install python 
    pyenv install 3.8.7
    pyenv global 3.8.7

    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
   SHELL

  config.trigger.after :up do |trigger|
    trigger.name = "Launching App"
    trigger.info = "Running the TODO app setup script" 
    trigger.run_remote = {privileged: false, inline: "
      
      cd /vagrant/
      poetry install
   
      nohup poetry run flask run --host 0.0.0.0 > log.txt 2>&1 &
    "}
  end
end
