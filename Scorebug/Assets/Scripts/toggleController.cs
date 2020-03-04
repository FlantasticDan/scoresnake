using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class toggleController : MonoBehaviour
{
    public Color lightColor;
    public Color darkColor;
    public colorkeeper masterController;
    public Image lightColorDisplay;
    public Image darkColorDisplay;
    
    // Start is called before the first frame update
    void Start()
    {
        lightColorDisplay.color = lightColor;
        darkColorDisplay.color = darkColor;
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void changeColor(bool newState)
    {
        if (newState)
        {
            masterController.updateColor(lightColor, darkColor);
        }
    }
}
