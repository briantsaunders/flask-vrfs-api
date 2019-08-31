# Small Example Flask API with VRFs

This is a small example API that allows you to GET, POST, and DELETE [VRFs](https://www.kernel.org/doc/Documentation/networking/vrf.txt) on a linux host.  This is meant to be an example of how I like to develop python api's using [flask](https://flask.palletsprojects.com/en/1.1.x/) in conjunction with the [flask-apispec](https://github.com/jmcarp/flask-apispec) library.

## Vagrant Environment

Within this repo I've included a vagrant file if you'd like to run it locally.  You should have vagrant and virtualbox installed prior to bringing up the vagrant environment.

### Vagrant Up

```
git clone https://github.com/briantsaunders/flask-vrfs-api.git
cd flask-vrfs-api
vagrant up
```

Ansible is used to provision the vagrant box.  It installs pip3 and the app development requirements.  The vagrant file will port forward port 5000 to the vagrant box so when you run the app within the vagrant box you can send requests from your local machine.

### Testing in Vagrant

Once the vagrant environment is up issue the following commands to run the app.

```
vagrant ssh
cd /vagrant
sudo python3 manage.py
```

From your local machine you should now be able to hit the swagger docs at http://localhost:5000/api/docs.  If you use postman on your local machine you can hit the API from that as well at http://localhost:5000/api/vrfs.