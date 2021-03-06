Orbital Evolution of the Proxima Centauri System
=================

Overview
--------

Possible scenario of the co-evolution of the orbits of Proxima b and Proxima c.

===================   ============
**Date**              6/24/20
**Author**            Joseph Livesey
**Modules**           DistOrb
                      EqTide
                      STELLAR
**Approx. runtime**   5 minutes
===================   ============

This simulation uses the CPL model of tidal evolution, employing the stellar, eqtide, and distorb modules. The final values of eccentricity (Mascareño et al. 2020) and semimajor axis (Anglada-Escudé et al. 2016) for Proxima b are satisfied at the end of the 7 Gyr run.

To run this example
-------------------

.. code-block:: bash

    vplanet vpl.in
    python makeplot.py <pdf | png>

Expected output
---------------

.. figure:: 2deg.png
   :width: 150px
   :align: center

.. figure:: 20deg.png
   :width: 150px
   :align: center

The figures above show a possible evolutionary scenario for the eccentricity, inclination, semimajor axis, and rotational period of Proxima b's orbit and the eccentricity and inclination of Proxima c's orbit. The first figure illustrates the case in which there is initially a 2º mutual inclination between b and c, while the second illustrates the case in which there is a 20º initial mutual inclination. The black dashed lines indicate the observed present-day values of Proxima b's orbital eccentricity and semimajor axis.
