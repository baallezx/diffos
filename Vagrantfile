# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
	config.vm.box = "hashicorp/precise32"
	config.vm.provider "virtualbox" do
		v.name = "tcp_client"
		v.memory = "512"
	end

	config.vm.provision "shell", inline <<-SHELL
		sudo apt-get install python vim tree ruby gem -y
	SHELL
end
