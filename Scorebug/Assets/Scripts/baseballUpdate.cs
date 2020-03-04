using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class baseballUpdate : MonoBehaviour
{
    // UI Elements
    public scorekeeper scorekeeper;
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
            UpdateOutsLabel();
            
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
        target.text = scorekeeper.score[field];
    }


    void UpdateOutsLabel()
    {
        if (int.Parse(scorekeeper.score["outs"]) == 1)
        {
            outsLabel.text = "OUT";
        }
        else
        {
            outsLabel.text = "OUTS";
        }
    }
    void UpdateBaseUI(RawImage img, string field)
    {
        bool state = bool.Parse(scorekeeper.score[field]);
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
        bool top = bool.Parse(scorekeeper.score["top"]);
        bool bottom = bool.Parse(scorekeeper.score["bottom"]);

        if (top && !bottom)
        {
            inningIndicator.eulerAngles = new Vector3(0.0f, 0.0f,00.0f);
            
        }

        if (!top && bottom)
        {
            inningIndicator.eulerAngles = new Vector3(0.0f, 0.0f,180.0f);
        }
    }
}
