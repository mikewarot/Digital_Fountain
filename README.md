Digital_Fountain
================

This project eventually will be a python implementation of a digital fountain. I've heard of them, read a little bit about them, but really don't understand the terminilogy found on the Wikipedia page on the subject. As such, this will be created from scratch by someone who is otherwise novice to the subject
My first approach is to use python, a language I have a passing familiarity with, to do the implementation.

The goal of a digital fountain is to deliver a file by breaking it into a stream of of blocks, such that recovering the data from a sufficient number of blocks recovers the file. Like a bucked of water gathering mist from a real fountain, it doesn't matter which drops you get, eventually you can get a gallon of water.

To do this with data is non-trivial, to say the least. Here's my basic idea:

Break a file into N blocks, zero padded on the end.
K is a combination factor (how many blocks we XOR together)

for a given transmittion packet number, I:
  set the python random seed to I
  use set.sample to get a list of K blocks to combine
  zero the output data block to zero
  XOR the output with eack of the chosen data blocks
  MD5 or other checksum on the packet (sequence number, XORed data)
  transmit packet
  increment I

using the knowledge of I, and the same pseudo-random generation code, the list of K blocks doesn't need transmission

to recieve the complete file, it's necessary to treat the packets that do arrive as puzzle pieces, and work backwards to get the original file from the pieces we do have.

I don't know how to choose an efficient K, or block size, or anything else... I'll get there, though.

Mike Warot - December 30, 2012
