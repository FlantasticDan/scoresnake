using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class teamkeeper : MonoBehaviour
{
    public TextMeshProUGUI teamLabel;

    public void updateTeamName(string newName)
    {
        teamLabel.text = newName;
    }
}
