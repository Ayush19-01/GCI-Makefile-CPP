all: squares.cpp
		$ g++ squares.cpp -o final
		./final | $ python3 graph.py

clean:
		rm final
