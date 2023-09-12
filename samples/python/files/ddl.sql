-- Copyright (c) 2023 Broadcom. All rights reserved. The term
-- "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.
-- 
-- This software and all information contained therein is confidential
-- and proprietary and shall not be duplicated, used, disclosed or
-- disseminated in any way without the express written permission of
-- Broadcom. All authorized reproductions must be marked with this
-- language.
-- 
-- TO THE EXTENT PERMITTED BY APPLICABLE LAW, BROADCOM PROVIDES THIS
-- SOFTWARE "AS IS" WITHOUT WARRANTY OF ANY KIND, INCLUDING WITHOUT
-- LIMITATION, ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
-- PARTICULAR PURPOSE OR NONINFRINGEMENT. IN NO EVENT WILL BROADCOM BE
-- LIABLE TO THE END USER OR ANY THIRD PARTY FOR ANY LOSS OR DAMAGE,
-- DIRECT OR INDIRECT, FROM THE USE OF THIS MATERIAL, INCLUDING WITHOUT
-- LIMITATION, LOST PROFITS, BUSINESS INTERRUPTION, GOODWILL, OR LOST
-- DATA, EVEN IF BROADCOM IS EXPRESSLY ADVISED OF SUCH LOSS OR DAMAGE.


CREATE  TABLE DEV.DBMTB
        ( COL1 CHAR ( 1 )                                                       
        , COL2 CHAR ( 2 )                                                       
        , COL3 CHAR ( 3 )                                                       
        )                                                                       
        IN DBMDB.DBMTS                                                          
   CCSID         EBCDIC                                                         
   ;

CREATE  TABLE DEV2.DBMTB2
       ( COL1 CHAR ( 1 )
       , COL2 CHAR ( 2 )
       , COL3 CHAR ( 3 )
       )
       IN DBMDB.DBMTS                                                          
   CCSID         EBCDIC
;
