Steam-to-Ethylene Ratio
==================================================

.. math::

   \text{}

.. raw:: html

   <style>
      .kpi-table {
         width: 100%; border-collapse: collapse; margin-bottom: 1.5em;
         border: 1px solid #e0e0e0; table-layout: fixed;
      }
      .kpi-table td {
         padding: 12px; vertical-align: top; border: 1px solid #e0e0e0;
         word-wrap: break-word;
      }
      .kpi-table td:first-child {
         width: 25%; font-weight: bold; background-color: #f7f7f7;
      }
      .kpi-table ul { list-style-type: disc; padding-left: 20px; margin: 0; }
      .kpi-table .math-equation {
         text-align: center; margin: 1em 0; overflow-x: auto; padding: 5px;
      }
      .kpi-table .formula-notes li { margin-bottom: 0.5em; }
      .kpi-table .formula-notes i { font-family: 'Times New Roman', serif; }
      .btn { display:inline-block; padding:8px 12px; border-radius:6px; color:#fff; text-decoration:none; font-weight:500; font-size:13px; }
      .btn-vscode { background-color:#2c5282; }
      .btn-pycharm { background-color:#000; }
      .btn-edit { background-color:#4a7c59; }
   </style>

   <div style="margin-bottom: 1.5em; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="font-size: 13px; font-weight: 500; color: #4a5568;">Open in:</span>
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/tsql_kpi_02.tsql:1" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/tsql_kpi_02.tsql&line=1" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=Steam-to-Ethylene%20Ratio" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>The Steam-to-Ethylene Ratio is a key performance indicator that measures the amount of steam used in the production of ethylene</li><li>It provides insight into the efficiency of the steam utilization in the ethylene production process</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of monitoring the Steam-to-Ethylene Ratio is to optimize the use of steam in ethylene production</li><li>thereby improving energy efficiency and reducing operational costs</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The ratio is calculated by dividing the volume of steam used by the volume of ethylene produced, ensuring that the ethylene value is not zero to avoid division errors.</p>
               <p>See code context for implementation details.</p>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               0.0s (AI 0.0s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 0.001s
                  • AI: 0.001s
                  • Render: 0.0s
               </div>
            </td>
         </tr>

         <tr>
            <td>Extraction rate %</td>
            <td>88.9%</td>
         </tr>
         <tr>
            <td>Error rate %</td>
            <td>11.1%</td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>This KPI is used in evaluating the efficiency of ethylene production processes and can inform decisions related to process optimization and resource allocation</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for this KPI are the volumes of steam and ethylene produced during the manufacturing process</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for the Steam-to-Ethylene Ratio is dimensionless, as it is a ratio of two volumetric quantities.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The data for this KPI is typically sourced from production reports and operational data collected during the ethylene manufacturing process.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>A higher Steam-to-Ethylene Ratio may indicate excessive steam usage, which could lead to increased costs and reduced efficiency, while a lower ratio suggests better steam utilization.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: sql
      :linenos:
   
      :emphasize-lines: 1
   

      -- KPI: Steam-to-Ethylene Ratio
   SELECT CAST(steam AS FLOAT) / NULLIF(CAST(ethylene AS FLOAT), 0) AS [Steam-to-Ethylene Ratio]
   FROM (SELECT 1.8 AS steam, 1.0 AS ethylene) x;