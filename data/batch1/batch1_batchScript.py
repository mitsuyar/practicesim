ó
ÒfzXc           @   s¯   d  Z  d d l Z d d l m Z d d l m Z d d l m Z d d l Z d d l m	 Z	 e	 j
   Z e j   d k r e j d  n  d   Z d	 e f d
     YZ d S(   s[   
batch.py 

Class to setup and run batch simulations

Contributors: salvadordura@gmail.com
iÿÿÿÿN(   t   product(   t   popen2(   t   sleep(   t   hi    c         C   sq   d d l  m } m } d Gt j   GHd |  | f } | d GH| | j d  d | d | } | j j   GHd  S(	   Niÿÿÿÿ(   t   Popent   PIPEs   
Job in rank id: s   nrniv %s simConfig=%ss   
t    t   stdoutt   stderr(   t
   subprocessR   R   t   pct   idt   splitR   t   read(   t   scriptt   cfgSavePathR   R   t   commandt   proc(    (    sb   /private/var/folders/f7/zxsvws654x7820j20qvwbpl40000gp/T/pip-build-Bvg18f/netpyne/netpyne/batch.pyt   runJob   s    	!t   Batchc           B   s)   e  Z d  d d  Z d   Z d   Z RS(   s   cfg.pys   netParams.pyc         C   s]   d t  t j j    |  _ | |  _ | |  _ g  |  _ d |  j |  _ d |  _	 i  |  _
 d  S(   Nt   batch_t   /t   grid(   t   strt   datetimet   datet   todayt
   batchLabelt   cfgFilet   netParamsFilet   paramst
   saveFoldert   methodt   runCfg(   t   selfR   R   (    (    sb   /private/var/folders/f7/zxsvws654x7820j20qvwbpl40000gp/T/pip-build-Bvg18f/netpyne/netpyne/batch.pyt   __init__!   s    				c   	      C   só   d d  l  } | j j |  } | j |  d } | j d  d } y | j |  Wn/ t k
 r | j j |  s d G| GHq n Xi |  j d 6} | d k rï d d  l } d | GHt	 | d	  # } | j
 | | d
 d d t Wd  QXn  d  S(   Niÿÿÿÿi    t   .i   s    Could not createt   batcht   jsons   Saving batch to %s ... t   wt   indenti   t	   sort_keys(   t   ost   patht   basenameR   t   mkdirt   OSErrort   existst   __dict__R&   t   opent   dumpt   True(	   R"   t   filenameR*   R,   t   foldert   extt   dataSaveR&   t   fileObj(    (    sb   /private/var/folders/f7/zxsvws654x7820j20qvwbpl40000gp/T/pip-build-Bvg18f/netpyne/netpyne/batch.pyt   save*   s    	c      	   C   sÑ  |  j  d k rÍd d  l } d d  l } y | j |  j  Wn5 t k
 rr | j j |  j  ss d G|  j GHqs n X|  j d |  j d } |  j	 |  |  j d |  j d } | j
 d | j j t  d |  |  j d |  j d	 } | j
 d |  j d |  | j j |  j  j d
  d } t j | |  j  } | j |  _ t g  |  j D] } | d | d f ^ qY  \ } } t |   }	 t g  | D] }
 t t |
   ^ q  } |  j j d d   d k rx- t t t j     D] } t j   qíWn  xt | |	  D]s\ } } xJ t  |  D]< \ } } | | } t! |  j | |  | d t" |  GHq-W|  j d j# g  | D] } d j# d t" |   ^ q } | |  j _$ |  j |  j _ |  j d | d } |  j j	 |  |  j d | } |  j j d t%  r.| j | d  r.d | GHq|  j j d d   d k r-|  j j d d  } t& |  |  j j d d  } |  j j d d  } |  j j d d  } |  j j d d   } d! | } d" | | | f } t' d#  \ } } d$ | | | | | | | f } | j( |  | d% GH| j)   q|  j j d d   d k r|  j d | } d& G| GHt j* t+ |  j j d d  |  qqWy+ x t j,   rªt& d  qWt j-   Wn n Xt& d'  n  d  S((   NR   iÿÿÿÿs    Could not createR   s   _batch.jsons   _batchScript.pys   cp R   s   _netParams.pyR$   i    t   labelt   valuest   typet   mpis    = t    t   _s	   _cfg.jsont   skips   .jsons3   Skipping job %s since output file already exists...t
   hpc_torquet   sleepIntervali   t   numprocR   s   init.pyt   walltimes   00:30:00t	   queueNamet   defaults   nodes=1:ppn=%ds1   mpiexec -np %d nrniv -python -mpi %s simConfig=%st   qsubs`  #!/bin/bash 
                        #PBS -N %s
                        #PBS -l walltime=%s
                        #PBS -q %s
                        #PBS -l %s
                        #PBS -o %s.run
                        #PBS -e %s.err
                        cd $PBS_O_WORKDIR
                        echo $PBS_O_WORKDIR
                        %ss   
s   Submitting job i
   (.   R    R*   t   globR-   R   R.   R+   R/   R   R9   t   systemt   realpatht   __file__R   R,   R   R   t   impt   load_sourcet   cfgt   zipR   R    t   ranget   lenR!   t   gett   Nonet   intR
   t   nhostt	   runworkert	   enumeratet   setattrR   t   joint   simLabelt   FalseR   R   t   writet   closet   submitR   t   workingt   done(   R"   R*   RH   t
   targetFilet   cfgModuleNamet	   cfgModulet   pt	   labelListt
   valuesListt   valueCombinationst   xt   indexCombinationst   iworkert   iCombt   pCombt   it   paramValt
   paramLabelRZ   R   t   jobNameRB   RC   R   RD   RE   t   nodesppnR   t   outputt   inputt	   jobString(    (    sb   /private/var/folders/f7/zxsvws654x7820j20qvwbpl40000gp/T/pip-build-Bvg18f/netpyne/netpyne/batch.pyt   run>   sx    %"6+
<(

		)(   t   __name__t
   __module__R#   R9   Ru   (    (    (    sb   /private/var/folders/f7/zxsvws654x7820j20qvwbpl40000gp/T/pip-build-Bvg18f/netpyne/netpyne/batch.pyR      s   		(   t   __doc__R   t	   itertoolsR    R   t   timeR   RL   t   neuronR   t   ParallelContextR
   R   t   master_works_on_jobsR   t   objectR   (    (    (    sb   /private/var/folders/f7/zxsvws654x7820j20qvwbpl40000gp/T/pip-build-Bvg18f/netpyne/netpyne/batch.pyt   <module>   s    	
