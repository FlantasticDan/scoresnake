using System.Collections;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using Newtonsoft.Json;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class scorekeeper : MonoBehaviour
{
    public Dictionary<string, string> score;
    public Thread scoreKeeperServer;

    // UI Elements
    public TextMeshProUGUI visitorScore;
    public TextMeshProUGUI homeScore;
    public TextMeshProUGUI inning;
    public RectTransform inningIndicator;
    public TextMeshProUGUI balls;
    public TextMeshProUGUI strikes;
    public TextMeshProUGUI outsLabel;
    public TextMeshProUGUI outs;
    public RawImage firstBaseUI;
    public RawImage secondBaseUI;
    public RawImage thirdBaseUI;
    public Color emptyBase;
    public Color occupiedBase;

    // Start is called before the first frame update
    void Start()
    {
        scoreKeeperServer = new Thread(new ThreadStart(ScoreServer));
        scoreKeeperServer.Start();        
    }

    // Update is called once per frame
    void Update()
    {
        try
        {
            UpdateTextUI(visitorScore, "visitor");
            UpdateTextUI(homeScore, "home");
            UpdateTextUI(inning, "inning");
            UpdateTextUI(balls, "balls");
            UpdateTextUI(strikes, "strikes");
            UpdateTextUI(outs, "outs");
            
            UpdateBaseUI(firstBaseUI, "base1");
            UpdateBaseUI(secondBaseUI, "base2");
            UpdateBaseUI(thirdBaseUI, "base3");

            UpdateIndicator();
        }
        catch (System.Exception)
        {
            Debug.Log("Couldn't Update UI");
        }
    }


    void UpdateTextUI(TextMeshProUGUI target, string field)
    {
        target.text = score[field];
    }

    void UpdateBaseUI(RawImage img, string field)
    {
        bool state = bool.Parse(score[field]);
        if (state)
        {
            img.color = occupiedBase;
        }
        else
        {
            img.color = emptyBase;
        }
    }

    void UpdateIndicator()
    {
        bool top = bool.Parse(score["top"]);
        bool bottom = bool.Parse(score["bottom"]);

        if (top && !bottom)
        {
            inningIndicator.eulerAngles = new Vector3(0.0f, 0.0f,00.0f);
            
        }

        if (!top && bottom)
        {
            inningIndicator.eulerAngles = new Vector3(0.0f, 0.0f,180.0f);
        }
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
