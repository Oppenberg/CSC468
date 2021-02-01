import geni.portal as portal
import geni.rspec.pg as pg

request = portal.context.makeRequestRSpec()
node = request.XenVM("node")

node.disk_image = 
