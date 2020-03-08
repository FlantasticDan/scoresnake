using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class volleyballUpdate : MonoBehaviour
{
    public scorekeeper scorekeeper;
    public TextMeshProUGUI homeScore;
    public TextMeshProUGUI homeSets;
    public TextMeshProUGUI visitorScore;
    public TextMeshProUGUI visitorSets;
    public TextMeshProUGUI sets;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        try
        {
            UpdateTextUI(homeScore, "home");
            UpdateTextUI(visitorScore, "visitor");
            UpdateTextUI(homeSets, "home_sets");
            UpdateTextUI(visitorSets, "visitor_sets");
            UpdateSet();
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

    void UpdateSet()
    {
        string newText = "Set " + scorekeeper.score["set"];
        sets.text = newText;
    }
}
