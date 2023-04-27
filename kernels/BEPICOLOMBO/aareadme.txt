BepiColombo SPK files
===========================================================================

     This ``aareadme.txt'' file describes the contents of the kernels/spk
     directory of the BepiColombo SPICE data server.

     It was last modified on July 8th, 2021 by Ricardo Valles Blanco, ESAC/ESA.


Contact Information
--------------------------------------------------------

     If you have any questions regarding this directory or its
     contents, please contact the ESA SPICE Service at ESAC:

             Alfredo Escalante Lopez
             (+34) 91-8131-429
             spice@sciops.esa.int


References and required readings
--------------------------------------------------------

     1. ``SPK Required Reading'', NAIF Document


Brief Summary
--------------------------------------------------------

     This directory contains the SPICE SP-Kernel files for the BepiColombo
     mission, including mission analysis, nominal and operational spacecraft
     trajectory SPKs, generic planetary and satellite ephemeris SPKs.


File naming conventions
--------------------------------------------------------

   Naming Scheme for BepiColombo spacecraft SPKs:

     The naming scheme for the BepiColombo spacecraft SPKs is:

           bc_SC_TYPE[_ID][_DESC]_YYYYMMDD_YYYYMMDD_vNN.bsp

     where

           SC        acronym of the spacecraft:

                          mpo: for the Mercury Planetary Orbiter (MPO)
                               spacecraft;
                          mmo: for the Mercury Magnetospheric Orbiter (MMO)
                               spacecraft;
                          mtm: for the Mercury Transfer Module (MTM)
                               spacecraft

           TYPE      Data type, where a reference to the originator of the
                     data, the type of data and the and the reference period
                     is provided. This is a three letter acronym. The first
                     letter defines the file originator:

                          s: Science Operations Center;
                          m: Mission Analysis;
                          f: Flight Dynamics;

                     the second letter defines the reference period of the
                     data:

                          c: Cruise phase;
                          l: Science phase Long term;
                          m: Science phase Medium term;
                          s: Science phase Short term;
                          o: Undefined;

                     the third letter indicates the type of data

                          p: Predicted data;
                          r: Reconstructed data;
                          t: Test data;

           ID        mapping to the original file product IDs as defined
                     per an ICD document (optional);

           DESC      description of the original reference file of any
                     particular of the original file (optional);

           YYYYMMDD  coverage start and stop times in TDB (required);

           NN        version number, starting from 01 (required; e.g. 01);


     The naming scheme for the BepiColombo spacecraft center-of-gravity
     SPKs is:

            bc_SC_cog[_ID][_YYYYMMDD_YYYYMMDD]_vNN.bsp

     where

           SC        acronym of the spacecraft:

                          mpo: for the Mercury Planetary Orbiter (MPO)
                               spacecraft;
                          mmo: for the Mercury Magnetospheric Orbiter (MMO)
                               spacecraft;
                          mtm: for the Mercury Transfer Module (MTM)
                               spacecraft

           ID        mapping to the original file product IDs as defined
                     per an ICD document (optional);

           YYYYMMDD  coverage start and stop times in TDB (optional);

           NN        version number, starting from 01 (required; e.g. 01);


     The naming scheme for the BepiColombo spacecraft structures SPKs is:

           bc_SC_struct_vNN.bsp

     where

           SC        acronym of the spacecraft:

                          mpo: for the Mercury Planetary Orbiter (MPO)
                               spacecraft;
                          mmo: for the Mercury Magnetospheric Orbiter (MMO)
                               spacecraft;
                          mtm: for the Mercury Transfer Module (MTM)
                               spacecraft

           NN        version number, starting from 01 (required; e.g. 01);


     The naming scheme for BepiColombo Schulte vector points SPKs is:

           bc_mpo_schulte_vector_vNN.bsp

     where

           NN       version (required; e.g. 01);


   Naming Scheme for Generic Planetary Ephemeris SPKs

     The naming scheme for generic planetary SPKs is:

           deNNN.bsp

     where

           NNN       DE version (required; e.g. 421);


   Naming Scheme for ESA ESTRACK ground stations SPKs

     The naming scheme for ESA ESTRACK ground stations SPKs is:

           estrack_vNN.bsp

     where

           NN       version (required; e.g. 01);


   Naming Scheme for NASA DSN ground stations SPKs

     The naming scheme for NASA DSN ground stations SPKs is:

           earthstns_itrf93_YYYYMMDD.bsp

     where

           YYYYMMDD       product creation time (required);


   Naming Scheme for BepiColombo science frames origins SPKs

     The naming scheme for BepiColombo science frames origins SPKs is:

           bc_sci_vNN.bsp

     where

           NN       version (required; e.g. 01);


Current SPK Kernels Set
--------------------------------------------------------

   bc_mmo_mlt_XXXXX_YYYYMMDD_YYYYMMDD_vNN.bsp

      SPICE SPK file that contains MMO test trajectory for the
      science phase. This trajectory is delivered by Mission Analysis in the
      format of an OEM file or by file containing tabular ASCII information.
      XXXXX refers to the CReMA/Working Paper ID of the original trajectory
      file delivered by Mission Analysis. YYYYMMDD_YYYYMMDD indicates the
      coverage of the SPK. Created by the ESA SPICE Service (ESS).


   bc_mmo_cruise_vNN.bsp

      SPICE SPK file that contains Mercury Magnetosphetic Spacecraft (MMO)
      relative position with respect to MPO in order to bind MMO to the MPO
      trajectory. Created by the ESA SPICE Service (ESS).


   bc_mmo_slt_extension_YYYYMMDD_YYYYMMDD_vNN.bsp

      SPICE SPK file that contains MMO test trajectory for the extended
      science phase. Created by the ESA SPICE Service (ESS).


   bc_mmo_struct_vNN.bsp

      SPICE SPK file that contains MMO spacecraft structures positions that
      apply during all the mission. Created by the ESA SPICE Service (ESS).


   bc_mpo_cog_NNNNN_YYYYMMDD_YYYYMMDD_vNN.bsp

      SPICE SPK file that contains MPO spacecraft center-of-gravity (CoG)
      as delivered by the ESOC Flight Dynamics. It is important to note that
      the MPO trajectory SPK files provide ephemeris information for MPO (-121)
      and refer to the CoG. This file provides provides the position of
      MPO_SPACECRAFT (-121000). Created by the ESA SPICE Service (ESS).


   bc_mpo_cog_vNN.bsp

      SPICE SPK file that contains MPO spacecraft center-of-gravity (CoG)
      history. It is important to note that the MPO trajectory SPK files
      provide ephemeris information for MPO (-121) and refer to the CoG.
      This file provides provides the position of MPO_SPACECRAFT (-121000).
      Created by the ESA SPICE Service (ESS).


   bc_mpo_fcp_NNNNN_YYYYMMDD_YYYYMMDD_vNN.bsp

      SPICE SPK file that contains MPO spacecraft operational Sun centric
      ephemeris for the Cruise, Venus and Earth Flybys phases. This files
      contain both reconstructed and predicted data. This files should be
      considered final for the data period it covers.
      Created by the ESA SPICE Service (ESS).


   bc_mpo_fcp_Venus2SwingbyMTP_NNNNN_vNN.bsp

      SPICE SPK file that contains the sliced ephemeris of the MPO spacecraft
      as delivered by the ESOC Flight Dynamics for the period of the 2nd Venus
      Swingby. This file contains position data for the BepiColombo MPO
      spacecraft, 'MPO', relative to Mercury in the 'J2000' frame.
      Created by the ESA SPICE Service (ESS).


   bc_mpo_mcp_50034_20251205_20260314_vNN.bsp

      SPICE SPK file that contains MPO test trajectory for the mercury orbit
      insertion phase. This trajectory is delivered by Mission Analysis in the
      format of an OEM file or by file containing tabular ASCII information.
      50034 refers to the CReMA/Working Paper ID of the original trajectory
      file delivered by Mission Analysis. 20251205_20260314 indicates the
      coverage of the SPK. Created by the ESA SPICE Service (ESS).


   bc_mpo_mcp_50041_20181019_20251219_vNN.bsp

      SPICE SPK file that contains MPO test trajectory for the cruise phase.
      This trajectory is delivered by Mission Analysis in the format of an
      OEM file or by file containing tabular ASCII information.
      50041 refers to the CReMA/Working Paper ID of the original trajectory
      file delivered by Mission Analysis. 20181019_20251219 indicates the
      coverage of the SPK. Created by the ESA SPICE Service (ESS).


   bc_mpo_mlt_XXXXX_YYYYMMDD_YYYYMMDD_vNN.bsp

      SPICE SPK file that contains MPO test trajectory for the science
      phase. This trajectory is delivered by Mission Analysis in the format of
      an OEM file or by file containing tabular ASCII information. XXXXX
      refers to the CReMA/Working Paper ID of the original trajectory file
      delivered by Mission Analysis. YYYYMMDD_YYYYMMDD indicates the coverage
      of the SPK. Created by the ESA SPICE Service (ESS).


   bc_mpo_prelaunch_vNN.bsp

      SPICE SPK file that contains MPO trajectory for before the launch in
      order to have coverage before launch.
      Created by the ESA SPICE Service (ESS).


   bc_mpo_schulte_vector_vNN.bsp

      SPICE SPK file that contains MPO spacecraft structures positions involved
      in the Schulte vector computations. These apply during all the mission.
      Created by the ESA SPICE Service (ESS).


   bc_mpo_slt_extension_YYYYMMDD_YYYYMMDD_vNN.bsp

      SPICE SPK file that contains the ephemerides of the MPO spacecraft
      (BEPICOLOMBO MPO) propagated 2 years, starting from the last state at
      2028 MAY 29 14:02:03.177 UTC extracted from the Mercury phase test orbit
      provided by Mission Analysis. Created by the ESA SPICE Service (ESS).


   bc_mpo_struct_vNN.bsp

      SPICE SPK file that contains MPO spacecraft structures positions that
      apply during all the mission. Created by the ESA SPICE Service (ESS).


   bc_mtm_cruise_vNN.bsp

      SPICE SPK file that contains Mercury Transfer Module (MTM)
      relative position with respect to MPO in order to bind MTM to the MPO
      trajectory. Created by the ESA SPICE Service (ESS).


   bc_mtm_struct_vNN.bsp

      SPICE SPK file that contains MTM spacecraft structures positions that
      apply during all the mission. Created by the ESA SPICE Service (ESS).


   bc_sci_vNN.bsp

      SPICE SPK file that contains draft position information for the
      Science frames origins for BepiColombo mission.
      Created by the ESA SPICE Service (ESS).


   de432s.bsp

      SPICE SPK file containing JPL planetary ephemerides version DE432.
      Created by NAIF, JPL.


   earthstns_itrf93_050714.bsp
      Contains ephemeris data for NASA DSN stations relative to the terrestrial
      reference frame label 'ITRF93'. This file was released the 14th of July
      2005. Created by NAIF, JPL.


   estrack_vNN.bsp

      SPICE SPK file that defines the position for each of the ESA ESTRACK
      ground stations, as seen from the center of the Earth, in the
      topocentric frame defined in the corresponding ESTRACK FK.
      Created by the ESA SPICE Service (ESS).


Other directory contents
--------------------------------------------------------

     aareadme.txt         This file.


Particulars
--------------------------------------------------------

     Nothing to report.


Kernel File Details
--------------------------------------------------------

     The most detailed description of the data in a binary SPK file is
     provided in metadata included inside the comment area of the file.
     This information can be viewed using the utility programs COMMNT and
     SPACIT included in the NAIF Toolkit.


End of aareadme file.