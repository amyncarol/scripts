from custodian.custodian import Custodian
from custodian.vasp.handlers import VaspErrorHandler, FrozenJobErrorHandler, \
        UnconvergedErrorHandler, MeshSymmetryErrorHandler, MaxForceErrorHandler, \
        PotimErrorHandler, NonConvergingErrorHandler, WalltimeHandler 
from custodian.vasp.jobs import VaspJob


#/opt/openmpi-intel/bin/mpirun -np ${NPROCS} ${MYMPIPROG}
vasp_cmd = ['/opt/openmpi-intel/bin/mpirun', '-np', '32', '/home/yaocai/bin/vasp.5.3.3_jan17.vtst']
handlers = [VaspErrorHandler(), FrozenJobErrorHandler(),
            MeshSymmetryErrorHandler(), PotimErrorHandler(),
            NonConvergingErrorHandler()]
            #, WalltimeHandler()]
#gzipped = False
jobs = [VaspJob(vasp_cmd, final=True, suffix="", auto_npar=False)]
c = Custodian(handlers, jobs, max_errors=10)
c.run()

