#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <map>

using namespace std;

typedef pair<pair<string, int>, string> PPSIS;

// priority of protocols
map<string, int> Protocols = {
	{ "ICMP", 1 },
	{ "UDP", 2 },
	{ "RTM", 3 },
	{ "IGMP", 4 },
	{ "DNS", 5 },
	{ "TCP", 6 }
};

class BandwidthManager {
private:
	struct CompareProtocols {
		bool operator() (const PPSIS &a, const PPSIS &b) {
			if (Protocols[a.first.first] == Protocols[b.first.first]) {
				return a.first.second > b.first.second;
			}

			return Protocols[a.first.first] > Protocols[b.first.first];
		}
	};

	priority_queue<PPSIS, vector<PPSIS>, CompareProtocols> PriorityQ;

public:
	//receives a packet with specified protocol and payload
	void rcv(string protocol, string payload) {
		static int counter = 0;
		PriorityQ.push(make_pair(make_pair(protocol, counter++), payload));
	}

	//returns the payload of the packet which should be send
	string send() {
		if (PriorityQ.empty()) {
			return "Nothing to send!";
		}

		string result = PriorityQ.top().second;
		PriorityQ.pop();
		
		return result;
	}
};


int main() {

	cin.sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	BandwidthManager test;

	for (int i = 0; i < n; i++) {
		string command, Protocol, Payload;
		cin >> command;
		
		if (command == "rcv") {
			cin >> Protocol;
			cin >> Payload;
			
			test.rcv(Protocol, Payload);
		}
		else if (command == "send") {
			cout << test.send() << "\n";
		}
	}

	return 0;
}