Cooling Water Delta-T (°C
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
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/csv_kpi.cs:0" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/csv_kpi.cs&line=0" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=Cooling%20Water%20Delta-T%20%28%C2%B0C" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Cooling Water Delta-T measures the temperature difference between the inlet and outlet of cooling water systems</li><li>indicating the effectiveness of heat exchange processes</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of monitoring Cooling Water Delta-T is to ensure optimal cooling system performance</li><li>enhance energy efficiency</li><li>and prevent overheating of equipment</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The Cooling Water Delta-T is calculated by subtracting the inlet temperature of the cooling water from its outlet temperature.</p>
               <div class="math-equation">$$ \mathit{Result} = \mathit{Outlet\,C} - \mathit{Inlet\,C;\,\}\,\}} $$</div>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               7.4s (AI 7.4s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 7.438s
                  • AI: 7.437s
                  • Render: 0.001s
               </div>
            </td>
         </tr>

         <tr>
            <td>Extraction rate %</td>
            <td>100.0%</td>
         </tr>
         <tr>
            <td>Error rate %</td>
            <td>0.0%</td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>This KPI is used in various performance indicators related to cooling system efficiency and thermal management</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for this KPI are the temperatures of the cooling water at the inlet and outlet points</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for Cooling Water Delta-T is degrees Celsius (°C).</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>Data for this KPI is typically sourced from temperature sensors installed in the cooling water system.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>Regular monitoring of Cooling Water Delta-T can help identify potential issues in cooling systems, such as fouling or inadequate flow rates, which can lead to operational inefficiencies.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: csharp
      :linenos:
   

      // KPI: Cooling Water Delta-T (°C)
   public static class CoolingWater
   {
       public static double DeltaT(double inlet_c, double outlet_c)
       {
           // ΔT = outlet - inlet
           return outlet_c - inlet_c;
       }
   }