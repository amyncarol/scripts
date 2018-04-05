from custodian.custodian import Custodian
from custodian.vasp.handlers import VaspErrorHandler, FrozenJobErrorHandler, \
        UnconvergedErrorHandler, MeshSymmetryErrorHandler, MaxForceErrorHandler, \
        PotimErrorHandler, NonConvergingErrorHandler, WalltimeHandler, \
	PositiveEnergyErrorHandler 
from custodian.vasp.jobs import VaspJob


vasp_cmd = ['mpirun', '-np', '4', '/home/yaocai/vtst/bin/vasp_std']
handlers = [VaspErrorHandler(), 
            PotimErrorHandler(), PositiveEnergyErrorHandler(),
            NonConvergingErrorHandler(change_algo=True),
 	    UnconvergedErrorHandler()]

jobs = [VaspJob(vasp_cmd, final=True, suffix="", auto_npar=False)]
c = Custodian(handlers, jobs, max_errors=5)
c.run()

