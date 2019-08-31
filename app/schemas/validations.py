# import third party libs
from marshmallow import ValidationError
from pyroute2 import IPDB


class Validations:
    """
    """

    def __init__(self):
        """
        """

    def validate_vrf(self, value):
        """
        """
        with IPDB() as ipdb:
            try:
                ipdb.interfaces[value]
            except KeyError:
                raise ValidationError(f"{value} is invalid")
            if ipdb.interfaces[value].kind != "vrf":
                raise ValidationError(f"{value} is not a vrf")

    def validate_vrf_name(self, value):
        """
        """
        vrf_names = []
        with IPDB() as ipdb:
            interface_ids = ipdb.by_index
            for interface_id in interface_ids:
                if ipdb.interfaces[interface_id].kind == "vrf":
                    vrf_names.append(ipdb.interfaces[interface_id].ifname)
        if value in vrf_names:
            raise ValidationError(f"{value} already exists")

    def validate_vrf_table(self, value):
        """
        """
        vrf_tables = []
        with IPDB() as ipdb:
            interface_ids = ipdb.by_index
            for interface_id in interface_ids:
                if ipdb.interfaces[interface_id].kind == "vrf":
                    vrf_tables.append(ipdb.interfaces[interface_id].vrf_table)
        if value in vrf_tables:
            raise ValidationError(f"{value} already exists")
