using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class customization : MonoBehaviour
{
    public GameObject configCanvas;
    private bool fullscreen = false;
    // Start is called before the first frame update
    void Start()
    {
        Screen.SetResolution(960, 540, FullScreenMode.Windowed);
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.F1))
        {
            configCanvas.SetActive(!configCanvas.activeSelf);
            Cursor.visible = configCanvas.activeSelf;
        }

        if (Input.GetKeyDown(KeyCode.F2))
        {
            if (fullscreen)
            {
                Screen.SetResolution(960, 540, FullScreenMode.Windowed);
                fullscreen = false;
            }
            else
            {
                Screen.SetResolution(1920, 1080, FullScreenMode.FullScreenWindow);
                fullscreen = true;
            }
        }
    }
}
