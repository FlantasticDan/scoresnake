﻿using System.Collections;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using Newtonsoft.Json;
using UnityEngine;

public class scorekeeper : MonoBehaviour
{
    public Dictionary<string, string> score;
    public Thread scoreKeeperServer;
    public string serverEndpoint;

    // Start is called before the first frame update
    void Start()
    {
        scoreKeeperServer = new Thread(new ThreadStart(ScoreServer));
        scoreKeeperServer.Start();
        serverEndpoint = GetIP();
    }

    // Update is called once per frame
    void Update()
    {

    }

    private string GetIP()
    {
        string hostName = System.Net.Dns.GetHostName();
        IPHostEntry ipEntry = System.Net.Dns.GetHostEntry(hostName);
        IPAddress[] addr = ipEntry.AddressList;

        return addr[addr.Length - 1].ToString();

    }

    void ScoreServer()
    {
        UdpClient server = new UdpClient(42016);

        IPEndPoint remoteEP = new IPEndPoint(IPAddress.Any, 0);

        string previous_payload = "";
        string payload_string = "NONE";

        while (true)
        {
            var payload = server.Receive(ref remoteEP);
            payload_string = Encoding.UTF8.GetString(payload);
            if (payload_string != previous_payload)
            {
                score = JsonConvert.DeserializeObject<Dictionary<string, string>>(payload_string);
                previous_payload = payload_string;
            }
        }
    }
}
