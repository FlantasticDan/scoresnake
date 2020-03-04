using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class colorkeeper : MonoBehaviour
{
    public RawImage teamBG;
    public RawImage teamScoreBG;

    public void updateColor(Color light, Color dark)
    {
        teamBG.color = light;
        teamScoreBG.color = dark;
    }
}
