﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class customization : MonoBehaviour
{
    public GameObject configCanvas;
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.F1))
        {
            configCanvas.SetActive(!configCanvas.activeSelf);
            Cursor.visible = configCanvas.activeSelf;
        }
    }
}
