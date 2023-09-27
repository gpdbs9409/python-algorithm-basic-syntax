{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMAwzpZKUgXW/s3nA7wA8Ng",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/gpdbs9409/gpdbs9409_OSS/blob/main/covid19_statistics_skeleton.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aW2rvxD4ZPMx",
        "outputId": "babb4fad-29f8-463f-f7d3-0a04f42319f6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "### Korean Population by Region\n",
            "* Total population: 51669716\n",
            "\n",
            "| Region | Population | Ratio (%) |\n",
            "| ------ | ---------- | --------- |\n",
            "| Seoul | 9550227 | 37.6 |\n",
            "| Gyeongi | 13530519 | 30.9 |\n",
            "| Busan | 3359527 | 2.2 |\n",
            "| Gyeongnam | 3322373 | 1.7 |\n",
            "| Incheon | 2938429 | 8.6 |\n",
            "| Gyeongbuk | 2630254 | 1.6 |\n",
            "| Daegu | 2393626 | 2.4 |\n",
            "| Chungnam | 2118183 | 3.6 |\n",
            "| Jeonnam | 1838353 | 1.3 |\n",
            "| Jeonbuk | 1792476 | 1.6 |\n",
            "| Chungbuk | 1597179 | 1.6 |\n",
            "| Gangwon | 1536270 | 1.9 |\n",
            "| Daejeon | 1454679 | 0.9 |\n",
            "| Gwangju | 1441970 | 2.3 |\n",
            "| Ulsan | 1124459 | 1.2 |\n",
            "| Jeju | 675883 | 0.3 |\n",
            "| Sejong | 365309 | 0.2 |\n",
            "\n"
          ]
        }
      ],
      "source": [
        "# Skeleton code\n",
        "def normalize_data(n_cases, n_people, scale):\n",
        "    # TODO) Calculate the number of cases per its population\n",
        "    norm_cases = []\n",
        "    for idx, n in enumerate(n_cases):\n",
        "        norm_cases.append(n / (n_people[idx] / scale))\n",
        "    return norm_cases\n",
        "\n",
        "# Given data\n",
        "regions = ['Seoul', 'Gyeongi', 'Busan', 'Gyeongnam', 'Incheon', 'Gyeongbuk', 'Daegu', 'Chungnam',\n",
        "           'Jeonnam', 'Jeonbuk', 'Chungbuk', 'Gangwon', 'Daejeon', 'Gwangju', 'Ulsan', 'Jeju', 'Sejong']\n",
        "n_people = [9550227, 13530519, 3359527, 3322373, 2938429, 2630254, 2393626, 2118183, 1838353,\n",
        "            1792476, 1597179, 1536270, 1454679, 1441970, 1124459, 675883, 365309]\n",
        "n_covid = [644, 529, 38, 29, 148, 28, 41, 62, 23, 27, 27, 33, 16, 40, 20, 5, 4]\n",
        "\n",
        "# Calculate total population and total new cases\n",
        "sum_people = sum(n_people)\n",
        "sum_covid = sum(n_covid)\n",
        "\n",
        "# Normalize COVID-19 data per 1 million people\n",
        "norm_covid = normalize_data(n_covid, n_people, 1000000)  # The new cases per 1 million people\n",
        "\n",
        "# Print population by region\n",
        "print('### Korean Population by Region')\n",
        "print('* Total population:', sum_people)\n",
        "print()\n",
        "print('| Region | Population | Ratio (%) |')\n",
        "print('| ------ | ---------- | --------- |')\n",
        "for idx, pop in enumerate(n_people):\n",
        "    ratio = (n_covid[idx] / sum_covid) * 100  # Calculate the ratio of new cases to the total\n",
        "    print('| %s | %d | %.1f |' % (regions[idx], pop, ratio))\n",
        "print('')\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# Print COVID-19 new cases by region\n",
        "print('Korean COVID-19 New Cases by Region')\n",
        "print('| Region | New Cases | Ratio (%) | New Cases per 1M People |')\n",
        "print('| ------ | --------- | --------- | ------------------------ |')\n",
        "for idx, cases_per_million in enumerate(norm_covid):\n",
        "    ratio = (n_covid[idx] / sum_covid) * 100\n",
        "    print('| %s | %d | %.1f | %.1f |' % (regions[idx], n_covid[idx], ratio, cases_per_million))\n",
        "\n"
      ],
      "metadata": {
        "id": "uwD2ByazZUbk"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}