#  Makefile for nasm program

all:sample sumprog adddigits addition toupper

ARCH=$(shell uname -m)

ifeq ($(ARCH),x86_64)
	NASM_FLAGS=-f elf32
	LD_FLAGS=-m elf_i386
else
	NASM_FLAGS=-f elf
	LD_FLAGS=
endif

sample: io.o sample.o
	ld $(LD_FLAGS) -o $@  $^
sumprog: io.o sumprog.o
	ld $(LD_FLAGS) -o $@  $^
adddigits: io.o adddigits.o
	ld $(LD_FLAGS) -o $@  $^
toupper: io.o toupper.o
	ld $(LD_FLAGS) -o $@  $^
addition: io.o addition.o
	ld $(LD_FLAGS) -o $@  $^

sample.o: sample.asm
	nasm  $(NASM_FLAGS) $<
toupper.o: toupper.asm
	nasm  $(NASM_FLAGS) $<
addition.o: addition.asm
	nasm  $(NASM_FLAGS) $<
sumprog.o: sumprog.asm
	nasm  $(NASM_FLAGS)  $<
adddigits.o: adddigits.asm
	nasm  $(NASM_FLAGS) $<
.PHONY: clean

clean:
	$(RM) sample.o  sumprog.o sample sumprog adddigits adddigits.o addition.o addition toupper toupper.o
