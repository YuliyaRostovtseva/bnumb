%module Bnumb
%{
/* Includes the header in the wrapper code */
#include "Bnumb.h"
%}

/* Parse the header file to generate wrappers */
%include "Bnumb.h"
