# third party libs
from pyroute2 import IPDB


class VrfOperations:
    """
    """

    def __init__(self):
        """
        """
        pass

    def _get_vrf_dict(self, ipdb, vrf_id):
        """
        """
        vrf = {
            "vrf_id": vrf_id,
            "name": ipdb.interfaces[vrf_id].ifname,
            "table": ipdb.interfaces[vrf_id].vrf_table,
        }
        return vrf

    def create_vrf(self, kwargs):
        """
        """
        with IPDB() as ipdb:
            with ipdb.create(
                kind="vrf", ifname=kwargs["name"], vrf_table=kwargs["table"]
            ) as i:
                i.up()
            vrf = self._get_vrf_dict(ipdb, ipdb.interfaces[kwargs["name"]].index)
        return vrf

    def delete_vrf(self, vrf_id):
        """
        """
        with IPDB() as ipdb:
            with ipdb.interfaces[vrf_id] as i:
                i.down()
                i.remove()

    def get_vrf(self, vrf_id):
        with IPDB() as ipdb:
            vrf = self._get_vrf_dict(ipdb, vrf_id)
        return vrf

    def get_vrfs(self):
        """
        """
        vrfs = []
        with IPDB() as ipdb:
            interface_ids = ipdb.by_index
            for interface_id in interface_ids:
                if ipdb.interfaces[interface_id].kind == "vrf":
                    vrfs.append(self._get_vrf_dict(ipdb, interface_id))
        return vrfs
