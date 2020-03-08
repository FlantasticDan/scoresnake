using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class customization : MonoBehaviour
{
    public GameObject configCanvas;
    public RectTransform scoreCanvas;
    public Camera mainCamera;
    public Color chromaColor;
    public Color lumaColor;
    public RectTransform option5;
    public RectTransform option4;
    public RectTransform option3;
    public RectTransform option2;
    public RectTransform option1;
    private bool fullscreen = false;
    private bool chroma = true;

    // Start is called before the first frame update
    void Start()
    {
        Screen.SetResolution(960, 540, FullScreenMode.Windowed);
        mainCamera.backgroundColor = chromaColor;
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

        if (Input.GetKeyDown(KeyCode.F3))
        {
            if (chroma)
            {
                mainCamera.backgroundColor = lumaColor;
                chroma = false;
            }
            else
            {
                mainCamera.backgroundColor = chromaColor;
                chroma = true;
            }
        }

        // Scorebug Positioning
        if (Input.GetKeyDown(KeyCode.F8))
        {
            scoreCanvas.transform.position = option5.transform.position;
            scoreCanvas.transform.localScale = option5.transform.localScale;
        }
        if (Input.GetKeyDown(KeyCode.F9))
        {
            scoreCanvas.transform.position = option4.transform.position;
            scoreCanvas.transform.localScale = option4.transform.localScale;
        }
        if (Input.GetKeyDown(KeyCode.F10))
        {
            scoreCanvas.transform.position = option3.transform.position;
            scoreCanvas.transform.localScale = option3.transform.localScale;
        }
        if (Input.GetKeyDown(KeyCode.F11))
        {
            scoreCanvas.transform.position = option2.transform.position;
            scoreCanvas.transform.localScale = option2.transform.localScale;
        }
        if (Input.GetKeyDown(KeyCode.F12))
        {
            scoreCanvas.transform.position = option1.transform.position;
            scoreCanvas.transform.localScale = option1.transform.localScale;
        }
    }
}
