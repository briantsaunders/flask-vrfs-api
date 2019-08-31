# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "geerlingguy/ubuntu1804"
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  ####################
  ## Provision Env ###
  ####################
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "pb.conf.all.yml"
  end
end
